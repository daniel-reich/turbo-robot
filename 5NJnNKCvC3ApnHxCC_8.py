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

def mubashir_function(a, b):
  check = all(n > 9 for n in [a, b])
  plus = max(a, b)
  minus = min(a, b)
  rslt = a * b
  return int(str(rslt)[0]) if check and a == b else int(str(minus)[::-1]) if check and plus > minus else rslt

