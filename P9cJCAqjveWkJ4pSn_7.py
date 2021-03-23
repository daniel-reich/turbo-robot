"""


Create a function that takes two integers and checks if they are equal.

### Examples

    is_equal(5, 6) ➞ False
    
    is_equal(1, 1) ➞ True
    
    is_equal("1", 1) ➞ False

### Notes

If there is a string then it should return `False`.

"""

def is_equal(num1, num2):
  if isinstance(num1, str) or isinstance(num2, str):
    return False
  else: 
    return num1 == num2

