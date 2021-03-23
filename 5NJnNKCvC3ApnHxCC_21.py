"""


 **Mubashir** has written a mysterious function that takes two numbers `a` and
`b` and returns _multiplication?_. Solve the riddle of what Mubashir's
function is by having a look at some of the examples below.

### Examples

    mubashir_function(0, 1) ➞ 0
    
    mubashir_function(1, 2) ➞ 2
    
    mubashir_function(10, 10) ➞ 1

### Notes

  * Check the **Tests** tab for more examples.
  * This isn't really a coding challenge, more of a fun riddle ;)

"""

def digit_sum(n):
    ds = 0
    while n > 0:
        ds += (n % 10)
        n //= 10
    return ds
​
def mubashir_function(a, b):
    return digit_sum(a) * digit_sum(b)

