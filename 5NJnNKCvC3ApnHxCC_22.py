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
  def remove_zeros(num):
    num = str(num)
    if num != '0':
      return int(num.replace('0',''))
    else:
      return 0
  def reverser(num):
    return int(''.join(list(reversed(str(num)))))
  
  if len(str(remove_zeros(a))) != 1 or len(str(remove_zeros(b))) != 1:
    return reverser(min([a, b]))
  else:
    return remove_zeros(a) * remove_zeros(b)

