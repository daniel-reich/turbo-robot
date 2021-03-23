"""


Given a list of _math equations_ (given as strings), return the **percentage
of correct answers** _as a string_. Round to the nearest _whole number_.

### Examples

    mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"]) ➞ "75%"
    
    mark_maths(["1-2=-2"]), "0%"
    
    mark_maths(["2+3=5", "4+4=9", "3-1=2"]) ➞ "67%"

### Notes

  * You can expect only _addition_ and _subtraction_.
  * Note how there aren't any spaces in any given equation.

"""

def mark_maths(lst):
  x = 0
  for i in lst:
    i = i.split("=")
    if eval(i[0]) == int(i[1]):
      x+=1
  return str(round(x/len(lst)*100)) + "%"

