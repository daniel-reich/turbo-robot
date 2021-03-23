"""


Create a function that takes a list of two numbers and checks if the **square
root** of the first number is equal to the **cube root** of the second number.

### Examples

    check_square_and_cube([4, 8]) ➞ True
    
    check_square_and_cube([16, 48]) ➞ False
    
    check_square_and_cube([9, 27]) ➞ True

### Notes

  * Remember to return either `True` or `False`.
  * All lists contain _two positive numbers_.

"""

def check_square_and_cube(lst):
 x=lst[1]/lst[0]
 if x**2==lst[0] and x**3==lst[1]:
  return True
 return False

