"""


Create a function that takes a string, checks if it has the same number of
"x"s and "o"s and returns either `True` or `False`.

  * Return a boolean value (`True` or `False`).
  * Return `True` if the amount of x's and o's are the same.
  * Return `False` if they aren't the same amount.
  * The string can contain any character.
  * When "x" and "o" are not in the string, return `True`.

### Examples

    XO("ooxx") ➞ True
    
    XO("xooxx") ➞ False
    
    XO("ooxXm") ➞ True
    # Case insensitive.
    
    XO("zpzpzpp") ➞ True
    # Returns True if no x and o.
    
    XO("zzoo") ➞ False

### Notes

  * Remember to return `True` if there aren't any x's or o's.
  * Must be case insensitive.

"""

def XO(txt):
  x = txt.lower().count("x")
  o = txt.lower().count("o")
  return x == o

