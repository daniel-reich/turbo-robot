"""


Given a list of integers `lst`, implement a function that returns the index of
the number nearest to the given value `n`. If two numbers equally distant from
`n` are found, the function will return the greatest of them.

### Examples

    nearest_element(10, [1, 100, 1000]) ➞ 0
    # 1 is the number nearest to 10.
    
    nearest_element(50, [100, 49, 51]) ➞ 2
    # 49 and 51 are equally distant from 50, with 51 being the greatest.
    
    nearest_element(-20, [-50, -10, -30]) ➞ 1
    # -10 and -30 are equally distant from -20, with -10 being the greatest.

### Notes

Integers in `lst` will always be unique.

"""

def nearest_element(n, lst):
  nearest = min([abs(i-n) for i in lst])
  return lst.index(max([i for i in lst if abs(i-n) == nearest]))

