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

def reverse(str):
  return reverse(str[1:]) + str[0] if str else str

