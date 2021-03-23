"""
Create a function whose return value always passes equality checks.

### Examples

    equals() == 0 ➞ True
    
    equals() == [] ➞ True
    
    equals() == (lambda: 1) ➞ True

### Notes

The challenge is passable.

"""

def equals():
  class Homogeneity:
    def __eq__(self, whatever):
      return True
  return Homogeneity()

