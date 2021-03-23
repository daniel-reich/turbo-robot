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
  return short_circuit()
​
class short_circuit:
​
  def __eq__(self,other):
    return True

