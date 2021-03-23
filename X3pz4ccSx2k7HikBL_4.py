"""


Wild Roger is participating in a _Western Showdown_ , meaning he has to draw
(pull out and shoot) his gun faster than his opponent in a gun standoff.

Given two strings,`p1` and `p2`, return which person drew their gun the
**fastest**. If both are drawn at _the same time_ , return `"tie"`.

### Examples

    showdown(
      "   Bang!        ",
      "        Bang!   "
    ) ➞ "p1"
    
    # p1 draws his gun sooner than p2
    
    showdown(
      "               Bang! ",
      "             Bang!   "
    ) ➞ "p2"
    
    showdown(
      "     Bang!   ",
      "     Bang!   "
    ) ➞ "tie"

### Notes

Both strings are the same length.

"""

def showdown(p1, p2):
  t1 = p1.index('Bang!')
  t2 = p2.index('Bang!')
  return 'p1' if t1 < t2 else 'p2' if t1 > t2 else 'tie'

