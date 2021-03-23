"""


Write a function that returns `True` if an integer can be expressed as a power
of base value 2 and `False` otherwise.

### Examples

    power_of_two(32) ➞ True
    
    power_of_two(1) ➞ True
    
    power_of_two(18) ➞ False

### Notes

N/A

"""

def power_of_two(num):
  return num in [2**x for x in range(0,int((num*3) **.5))]

