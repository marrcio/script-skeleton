Script-skeleton
===============

This little python program helps to create skeleton of "scripts".

Now, these scripts are not in the sense of Computer Programam scripts, but a human readable script.

For example, when transliterating a comic or Manga the following skeleton may be useful:

::

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

Such a structure can be obtained just by giving this::

  BFS-ish mode:
  """5pan:
  sq
  0
  sq(2part sidenote) sfx
  sfx 2b sfx
b sfx"""

or this::

  DFS-ish mode:
  """pan(sq)
  pan(0)
  pan(sq(2part sidenote) sfx)
  pan(sfx 2b sfx)
  pan(b sfx)"""

For a more complete documentation, check the project's `github project.
<https://github.com/marrcio/script-skeleton>`_.
