"""


Create a function that takes three integer arguments `(a, b, c)` and returns
the amount of integers which are of equal value.

### Examples

    equal(3, 4, 3) ➞ 2
    
    equal(1, 1, 1) ➞ 3
    
    equal(3, 4, 1) ➞ 0 

### Notes

Your function must return 0, 2 or 3.

"""

equal = lambda a, b, c: {3: 3, 1: 2, 0: 0}[(a==b)+(b==c)+(a==c)]

