# script-skeleton
A little helper for creating easily skeleton of scripts with hierarchy, to filled later.
So it generates something like this:

```
page1
    pan1
        sq1:

    pan2 - Nothing Here!
    pan3
        sq1
            part1:

            part2:

            sidenote1:

        sfx1:

    pan4
        sfx1:

        b1:

        b2:

        sfx2:

    pan5
        b1:

        sfx1:
```

Just by giving this:

```
BFS-ish mode:
"""5pan:
sq
0
sq(2part sidenote) sfx
sfx 2b sfx
b sfx"""
```

or

```
DFS-ish mode:
"""pan(sq)
pan(0)
pan(sq(2part sidenote) sfx)
pan(sfx 2b sfx)
pan(b sfx)"""
```

## How to use

Import the class.

```
$ ipython
from scriptskeleton.py import ScriptSkeleton
```

Give it a sring that resembles `identifier number identifier number`. Very forgiving, don't worry.
Example: "page1 page36", "block 3 block 50", "from the token 37 to the token66"
This will specify the name of the first level blocks and the number of them.
```
ss = ScriptSkeleton('page1 page36')
```

Now for every block created (e.g. 36 pages) feed it with internal blocks.
There are two possible ways of feeding: BFS-ish and DFS-ish.
For BFS-ish behaviour, give it a NUMBER, ID and end the line with':'. With this, the next NUMBER lines will specify what to give to blocks of ID.
For DFS-ish behaviour, give it NUMBER ID PARENTHESIS. Anything inside parenthesis will be a son of the current element.
For a empty element, put a line with a single 0

Illustrating this:
```
ss.feed("""5pan:
sq
0
sq(2part sidenote) sfx
sfx 2b sfx
b sfx""")
```

Means, in order of lines:
In the current block, create 5 'pan' which will be described in the next five lines.
on pan1, attach a 'sq' element.
on pan2, don't attach anything.
on pan3, attach a 'sq' which is father of 2 'part' element and a 'sidenode' and a 'sfx'
on pan4, attach a 'sfx', then 2 'b' then another 'sfx'
on pan5, attach a 'b' then a 'sfx'

Running this first would create the first example structure.

Once done, everything can be saved to a 'filename.txt' with:
```
ss.to_file('filename.txt')
```

PS. I know this README may be fuzzy and it may not seem as an useful program, but it was mostly written from me, to me. If you wish to use it, good luck.
