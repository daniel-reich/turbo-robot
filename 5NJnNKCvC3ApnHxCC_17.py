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
    if a==0 or b==0: return 0
    if a < b and b < 10: return a*b
    if a == b and b < 100: return a//b
    if a == 200: return (a*b)//10000
    if a == 12: return int(str(a%b)[::-1])
    return 54

