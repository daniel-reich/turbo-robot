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
    s1 = 0
    s2 = 0
    for i in range(len(holds)):
        if holds[i] == 'S':
            s1+= 50
        elif holds[i] == 'M':
            s1+=100
        elif holds[i] == 'L':
            s1+= 200
    for j in range(len(cargo)):
        s2+= cargo[j]
    if s1 >=s2:
        return True
    else:
        return False

