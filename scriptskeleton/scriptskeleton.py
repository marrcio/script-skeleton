import re
from collections import Counter

TAB_OF_SPACES = '    '
NOTHING_INDICATOR = " - Nothing Here!\n"
NAME_AND_NUMBER = re.compile(r"""
                             ([a-zA-Z!-@]+?)    # A name in a group
                             \s?            # Maybe a space
                             (\d+)          # A number
                             """, re.VERBOSE)
JUST_A_ZERO = re.compile(r"""
                         0                  # A single zero
                         \s*$               # Any number of spaces before the end
                         """, re.VERBOSE)
NUM_ID_TWOPOINTS = re.compile(r"""
                              (?P<num>\d+)?     # Maybe a number
                              (?P<id>.+?)       # An identifier
                              :\s*$             # : and any num of spaces
                              """, re.VERBOSE)
REST = re.compile(r"""
                  \S+
                  \s*$
                  """, re.VERBOSE)

NUM_ID_PARENTHESIS = re.compile(r"""
                                (?P<num>\d+)?
                                (?P<id>[a-zA-Z!-@]+?)
                                (?:                         # Don't capture all (with spaces)
                                 (?P<parenthesis>\(.+?\)) |
                                 \s+ |
                                 $
                                )
                                """, re.VERBOSE)

class ScriptSkeleton:
    def __init__(self, work_range, verbose=None):
        self.verbose = verbose if verbose is not None else False
        m = re.findall("[a-zA-Z]+\s?\d+", work_range)
        assert len(m) is 2
        self.master_unit, self.initial_block = re.search(NAME_AND_NUMBER, m[0]).groups()
        self.final_block = re.search("\d+", m[1]).group()
        self.master_padding = len(self.final_block)
        self.initial_block = int(self.initial_block)
        self.final_block = int(self.final_block)
        assert self.initial_block < self.final_block
        self.is_done = False
        self.children = [Block(self.master_unit + str(num).zfill(self.master_padding), 0)
                         for num in range(self.initial_block, self.final_block+1)]
        self._block_provider = iter(self.children).__next__
        self.curr_block = None

    def feed(self, string):
        try:
            self.curr_block = self._block_provider()
            self.curr_block.feed(string)
            if self.verbose:
                self.preview()
            else:
                print("Fed", self.curr_block.name + '.')
        except StopIteration:
            print("All pages fed.")

    def fuse_and_feed(self, string):
        self.feed(string)
        self.curr_block.fuse()
        self.feed("0")

    def status(self):
        if self.curr_block is None:
            print("Still not started.")
        elif re.search(str(self.final_block), self.curr_block.name):
            print("Work is over.")
        else:
            print("First block is", self.initial_block)
            print("Just worked block was", self.curr_block.name)
            print("Final block is", self.final_block)

    def preview(self, block_num=None):
        if block_num is None:
            print(str(self.curr_block))
        else:
            for block in self.children:
                if block.name == self.master_unit + str(block_num).zfill(self.master_padding):
                    print(str(block), end="")
                    break

    def redo(self, string, block_num=None):
        to_redo = None
        if block_num is None:
            to_redo = self.curr_block
        else:
            to_redo = self.children[block_num-self.initial_block]
        to_redo.clean()
        to_redo.feed(string)
        print("Fixed ", to_redo.name + '.')

    def to_file(self, filename):
        with open(filename, 'w') as f:
            print(*(child for child in self.children), sep="", file=f, end="")


class Block:
    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
        self.children = []

    def clean(self):
        self.children = []

    def fuse(self):
        num = int(re.search(r'\d+', self.name).group())
        self.name = self.name + '-' + str(num+1)

    def feed(self, string):
        """Feeds from a string to create the hierarchy of one block."""
        counter = Counter()
        string_list = string.split('\n')
        string_list = [elem for elem in string_list if elem]
        assert len(string_list) is not 0
        it = iter(string_list)
        for line in it:
            m_zero = re.match(JUST_A_ZERO, line)
            m_bfs = re.search(NUM_ID_TWOPOINTS, line)
            m_dfs = re.search(REST, line)
            if bool(m_zero):
                self.children = None
            elif bool(m_bfs):
                _num = m_bfs.group('num')
                _id = m_bfs.group('id')
                levels = int(_num) if _num is not None else 1
                for i in range(levels):
                    new_block = self.generate_empty_son(counter, _id)
                    self.children.append(new_block)
                    # Feeds the block with the next line
                    new_block.feed(next(it))
            elif bool(m_dfs):
                for m in re.finditer(NUM_ID_PARENTHESIS, line):
                    _num = m.group('num')
                    _id = m.group('id')
                    _parenthesis = m.group('parenthesis')
                    levels = int(_num) if _num is not None else 1
                    for i in range(levels):
                        new_block = self.generate_empty_son(counter, _id)
                        self.children.append(new_block)
                        # Feeds the block with the content of parenthesis, if it exists
                        if _parenthesis:
                            new_block.feed(_parenthesis[1:-1])

    def generate_empty_son(self, counter, _id):
        counter[_id] += 1
        if counter[_id] == 1:
            new_block = Block(_id, self.depth + 1)
        else:
            new_block = Block(_id + str(counter[_id]), self.depth + 1)
        return new_block

    def __str__(self):
        base = self.depth*TAB_OF_SPACES + self.name
        if self.children is None:
            return base + NOTHING_INDICATOR
        elif len(self.children) == 0:
            return base + ':\n' + self.depth*TAB_OF_SPACES + "\n"
        else:
            return base + "\n" + ('').join([str(child) for child in self.children])

    def __repr__(self):
        return "<Block=" + self.name + ", children_num=" + str(len(self.children))+">"
