"""


Create a function that takes a string and returns `True` or `False` depending
on whether or not the given formula is correct.

### Examples

    formula("6 * 4 = 24") ➞ True
    
    formula("18 / 17 = 2") ➞ False
    
    formula("") ➞ None

### Notes

  * You have to figure out what `a` is.
  * Ignore the spaces.
  * If the input is an empty string `""`, return `None`.
  * You do not need to dynamically find the value of `a` (it's a constant and the same accross all tests).

"""

def formula(txt):
  if len(txt) == 0:
    return None
  else:
    txt = "".join(txt.split()).replace("a", "4").split("=")
    result = True
    for i in range(len(txt) - 1):
      if eval(txt[i]) != eval(txt[i + 1]):
        result = False
    return result

