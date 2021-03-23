"""


Create a function that will remove the letters "a", "b" and "c" from the given
string and return the modified version. If the given string does not contain
"a", "b", or "c", return `None`.

### Examples

    remove_abc("This might be a bit hard") ➞ "This might e  it hrd"
    
    remove_abc("hello world!") ➞ None
    
    remove_abc("") ➞ None

### Notes

If the given string does not contain "a", "b", or "c", return `None`.

"""

def remove_abc(txt):
  if "a" in txt.lower() or "b" in txt.lower() or "c" in txt.lower():
    return txt.replace("a", "").replace("b", "").replace("c", "")
  else:
    return None

