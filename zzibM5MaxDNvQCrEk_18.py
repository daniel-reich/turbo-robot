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
​
  holds_size = []
  for hold in holds:
    if hold == 'S':
      holds_size.append(50)
    elif hold == 'M':
      holds_size.append(100)
    else:
      holds_size.append(200)
      
  for i in range(len(cargo)):
    current_space = holds_size[:]
    for j in range(len(holds_size)):
      if cargo[i] <= holds_size[j]:
        holds_size[j] -= cargo[i]
        break
    flag = True
    for j in range(len(holds_size)):
      if holds_size[j] != current_space[j]:
        flag = False
    if flag == True:
      return False
  return True

