"""
Create a function whose return value always passes equality checks.

### Examples

    equals() == 0 ➞ True
    
    equals() == [] ➞ True
    
    equals() == (lambda: 1) ➞ True

### Notes

The challenge is passable.

"""

class Equal:
  def __eq__(a,b):
    return True
def equals():
  return Equal()

