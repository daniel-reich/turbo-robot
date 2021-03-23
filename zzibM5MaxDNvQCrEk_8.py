"""


A ship has to transport cargo from one place to another, while picking up
cargo along the way. Given the total amount of cargo and the types of cargo
holds in the ship as lists, create a function that returns `True` if each
weight of cargo can fit in one hold, and `False` if it can't.

  * "S" means 50 cargo space.
  * "M" means 100 cargo space.
  * "L" means 200 cargo space.

### Examples

    will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]) ➞ True
    
    will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200]) ➞ False
    
    will_fit(["L", "L", "M"], [56, 62, 84, 90]) ➞ True

### Notes

N/A

"""

def will_fit(holds, cargo):
  i = 0
  fit = False
  for x in holds:
    if holds[i] == "S":
      if cargo[i] <= 50:
        fit = True
      else:
        fit = False
        break
    if holds[i] == "M":
      if cargo[i] <= 100:
        fit = True
      else:
        fit = False
        break
    if holds[i] == "L":
      if cargo[i] <= 200:
        fit = True
      else:
        fit = False
        break
    i += 1
  return fit

