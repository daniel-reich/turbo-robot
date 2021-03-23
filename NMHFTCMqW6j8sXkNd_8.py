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

from math import sqrt 
def check_square_and_cube(lst):
  print(sqrt(lst[0]) ,lst[1]**(1 / 3))
  return sqrt(lst[0]) == round(lst[1]**(1 / 3),2)

