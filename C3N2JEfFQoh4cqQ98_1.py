"""


Create a function that takes two strings as arguments and return either `True`
or `False` depending on whether the total number of characters in the first
string is equal to the total number of characters in the second string.

### Examples

    comp("AB", "CD") ➞ True
    
    comp("ABC", "DE") ➞ False
    
    comp("hello", "edabit") ➞ False

### Notes

  * Don't forget to `return` the result.
  * If you get stuck on a challenge, find help in the **Resources** tab.
  * If you're _really_ stuck, unlock solutions in the **Solutions** tab.

"""

def comp(a,b):
  return len(a) is len(b)

