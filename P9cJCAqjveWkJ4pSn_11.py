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
  return num1 == num2 and type(num1) != str and type(num2) != str

