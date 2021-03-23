"""


Create a function that takes two integers and checks if they are equal.

### Examples

    is_equal(5, 6) ➞ False
    
    is_equal(1, 1) ➞ True
    
    is_equal("1", 1) ➞ False

### Notes

If there is a string then it should return `False`.

"""

def is_equal(n1, n2): 
  if isinstance(n1, int) and isinstance(n2, int):
    return n1 == n2
  return False

