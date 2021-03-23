"""


Create a function that takes a list of numbers and return `"Boom!"` if the
digit 7 appears in the list. Otherwise, return `"there is no 7 in the list"`.

### Examples

    seven_boom([1, 2, 3, 4, 5, 6, 7]) ➞ "Boom!"
    # 7 contains the number seven.
    
    seven_boom([8, 6, 33, 100]) ➞ "there is no 7 in the list"
    # None of the items contain 7 within them.
    
    seven_boom([2, 55, 60, 97, 86]) ➞ "Boom!"
    # 97 contains the number seven.

### Notes

N/A

"""

def seven_boom(lst):
  import re
  if re.search("7", str(lst)) != None:
    return ("Boom!")
  else : return ("there is no 7 in the list")

