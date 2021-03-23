"""


Create a function (named fifth) that takes some arguments and returns the type
of the fifth argument. In case the arguments were less than 5, return `"Not
enough arguments"`.

### Examples

    fifth(1, 2, 3, 4, 5) ➞ int
    
    fifth("a", 2, 3, [1, 2, 3], "five") ➞ str
    
    fifth() ➞ "Not enough arguments"

### Notes

  * Don't get confused between zero-indexing and one-indexing.
  * If you get stuck check the **Resources** tab.

"""

def fifth(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
    
  if (len(Parameters) < 5):
    return "Not enough arguments"
  else:
    return type(Parameters[4])

