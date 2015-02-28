import re
from collections import Counter

TAB_OF_SPACES = '    '
NOTHING_INDICATOR = " - Nothing Here!\n"
NAME_AND_NUMBER = re.compile(r"""
                             ([a-zA-Z]+)    # A name in a group
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
                                (?P<id>[a-zA-Z]+)
                                (?:
                                 (?P<parenthesis>\(.+?\)) |
                                 \s+ |
                                 $
                                )
                                """, re.VERBOSE)

class ScriptSkeleton:
    def __init__(self, work_range):
        m = re.findall("[a-zA-Z]+\s?\d+", work_range)
        assert len(m) is 2
        master_unit, initial_block = re.search(NAME_AND_NUMBER, m[0]).groups()
        final_block = re.search("\d+", m[1]).group()
        master_padding = len(final_block)
        initial_block = int(initial_block)
        final_block = int(final_block)
        assert initial_block < final_block
        self.is_done = False
        self.children = [Block(master_unit + str(num).zfill(master_padding), 0)
                         for num in range(initial_block, final_block+1)]
        self._block_provider = iter(self.children).__next__

    def feed(self, string):
        try:
            block = self._block_provider()
            block.feed(string)
            print("Fed", block.name + '.')
        except StopIteration:
            print("All pages fed")

    def to_file(self, filename):
        with open(filename, 'w') as f:
            print(*(child for child in self.children), sep="", file=f, end="")


class Block:
    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
        self.children = []

    def feed(self, string):
        """Feeds from a string to create the hierarchy of one block."""
        counter = Counter()
        string_list = string.split('\n')
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
                    counter[_id] += 1
                    new_block = Block(_id + str(counter[_id]), self.depth + 1)
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
                        counter[_id] += 1
                        new_block = Block(_id + str(counter[_id]), self.depth + 1)
                        self.children.append(new_block)
                        # Feeds the block with the content of parenthesis, if it exists
                        if _parenthesis:
                            new_block.feed(_parenthesis[1:-1])

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