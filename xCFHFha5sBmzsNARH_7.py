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
  if len(txt) == 0:
    return txt
    
  else:
    
    first_letter = txt[0]
    
    return reverse(txt[1:]) + first_letter

