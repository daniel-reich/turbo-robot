"""


Noddy has written a mysterious function which takes in a word and returns
`True` if it's passed a specific test. Solve the riddle of what Noddy's
function is by having a look at some of the examples below.

### Examples

    noddy_function("FANTASTIC") ➞ True
    
    noddy_function("wonderful") ➞ False
    
    noddy_function("NODDY") ➞ False

### Notes

  * Check the **Tests** tab for more examples.
  * This isn't really a coding challenge, more of a fun riddle ;)

"""

def noddy_function(s):
  print(s)
  if "d" not in s and "D" not in s:
    return True
​
  else:
    return False

