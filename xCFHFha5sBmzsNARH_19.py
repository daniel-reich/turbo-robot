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
  if txt == "":
    return txt
  else:
    return reverse(txt[1:])+txt[0]

