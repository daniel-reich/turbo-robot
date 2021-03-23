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
  time1 = p1.index("B")
  time2 = p2.index("B")
  print(time1)
  print(time2)
  if time1 < time2:
    return("p1")
  else:
    if time1 > time2:
      return("p2")
    else:
      if time1 == time2:
        return("tie")

