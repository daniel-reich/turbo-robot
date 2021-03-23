"""


Given two numbers, return `True` if the sum of both numbers is less than 100.
Otherwise return `False`.

### Examples

    less_than_100(22, 15) ➞ True
    # 22 + 15 = 37
    
    less_than_100(83, 34) ➞ False
    # 83 + 34 = 117
    
    less_than_100(3, 77) ➞ true

### Notes

N/A

"""

less_than_100 = lambda a, b: a+b < 100

