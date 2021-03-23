"""


Create a function that reverses a `boolean` value and returns the string
`"boolean expected"` if another variable type is given.

### Examples

    reverse(True) ➞ False
    
    reverse(False) ➞ True
    
    reverse(0) ➞ "boolean expected"
    
    reverse(None) ➞ "boolean expected"

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def reverse(arg):
  if type(arg) != bool:
    return "boolean expected"
  else:
    return not arg

