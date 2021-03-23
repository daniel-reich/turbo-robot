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
  p1_index = 0
  p2_index = 0
  for i in range(0, len(p1)):
    if p1[i] == "B":
      p1_index = i
    if p2[i] == "B":
      p2_index = i
  if p1_index < p2_index:
    return "p1"
  elif p2_index < p1_index:
    return "p2"
  else:
    return "tie"

