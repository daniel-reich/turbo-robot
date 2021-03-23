"""
Create a function whose return value always passes equality checks.

### Examples

    equals() == 0 ➞ True
    
    equals() == [] ➞ True
    
    equals() == (lambda: 1) ➞ True

### Notes

The challenge is passable.

"""

class Truth:
​
  def __eq__(self, other):
    return True
​
def equals():
  val = Truth()
  return val

