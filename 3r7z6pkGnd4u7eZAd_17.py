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
  f = [eval(i.split("=")[0]) for i in lst]
  s = [int(i.split("=")[1]) for i in lst]
  return str(round((len([v for i,v in enumerate(f) if v == s[i]])/len(lst))*100))+"%"

