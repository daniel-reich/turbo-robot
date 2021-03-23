"""
Create a function whose return value always passes equality checks.

### Examples

    equals() == 0 ➞ True
    
    equals() == [] ➞ True
    
    equals() == (lambda: 1) ➞ True

### Notes

The challenge is passable.

"""

class Equals:
  def __call__(self):
    return self
  def __eq__(self, other):
    return True
​
equals = Equals()

