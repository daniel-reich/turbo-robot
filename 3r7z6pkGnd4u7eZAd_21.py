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
  print(lst) 
  total = len(lst)
  count = 0 
  for eqn in lst:
    equal_idx = eqn.index("=")
    for i in range(len(eqn)):
      if eqn[i] == "+":
        idx = i 
        if int(eqn[:idx]) + int(eqn[idx+1:equal_idx]) == int(eqn[equal_idx+1:]):
          count += 1 
      if eqn[i] == "-":
        idx = i 
        if idx < equal_idx:
          if int(eqn[:idx]) - int(eqn[idx+1:equal_idx]) == int(eqn[equal_idx+1:]):
            count += 1 
  return str(round((count/total) * 100)) + "%"

