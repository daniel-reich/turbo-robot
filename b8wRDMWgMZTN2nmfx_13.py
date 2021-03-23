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

def equal(a, b, c):
    if [a,b,c].count(a) == 1 and [a,b,c].count(b) == 1:
        return 0
    elif [a,b,c].count(a)>=[a,b,c].count(b):
        return [a,b,c].count(a)
    else:
        return [a,b,c].count(b)

