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
  if a < 10 and b < 10:
    return a*b
  elif a%10==0 and b%10==0:
    return int(str(a*b)[0])
  elif a%10 and b%10:
    return int(str(min([a,b]))[::-1])
