"""
Create a function whose return value always passes equality checks.

### Examples

    equals() == 0 ➞ True
    
    equals() == [] ➞ True
    
    equals() == (lambda: 1) ➞ True

### Notes

The challenge is passable.

"""

class crap:
  def __eq__(self,o):return 1
equals=lambda:crap()

