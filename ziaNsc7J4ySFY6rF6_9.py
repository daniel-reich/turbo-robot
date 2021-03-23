"""


A ship has to transport cargo from one place to another, while picking up
cargo along the way. Given the total amount of cargo and the types of cargo
holds in the ship as lists, create a function that returns `True` if all the
cargo can fit on the ship, and `False` if it can't.

  * "S" means 50 cargo space.
  * "M" means 100 cargo space.
  * "L" means 200 cargo space.

### Examples

    will_fit(["M", "L", "L", "M"], [56, 62, 84, 90]) ➞ True
    
    will_fit(["S", "S", "S", "S", "L"], [40, 50, 60, 70 , 80, 90, 200]) ➞ False
    
    will_fit(["L", "L", "M"], [56, 62, 84, 90]) ➞ True

### Notes

Calculate the cargo as a whole, and not for each seperate cargo hold (see
example #2).

"""

def will_fit(holds, cargo):
    x=0
    for i in holds:
        if i=='M':
            x+=100
        elif i=='S':
            x+=50
        elif i=='L':
            x+=200
    if sum(cargo)<x:
        return True
    else:
        return False

