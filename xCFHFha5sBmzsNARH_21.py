"""


Write a function that reverses a string. **Make your function recursive.**

###  Examples

    reverse("hello") ➞ "olleh"
    
    reverse("world") ➞ "dlrow"
    
    reverse("a") ➞ "a"
    
    reverse("") ➞ ""

### Notes

  * For non-base cases, your function must call itself at least once.
  * Check the **Resources** tab for info on recursion.

"""

def reverse(txt):
  if len(txt) in [0,1]:
    return txt
  else:
    return txt[-1]+reverse(txt[:-1])

