"""


Create a function that takes a string; we'll say that the front is the first
three characters of the string. If the string length is less than three
characters, the front is whatever is there. Return a new string, which is
three copies of the front.

### Examples

    front3("Python") ➞ "PytPytPyt"
    
    front3("Cucumber") ➞ "CucCucCuc"
    
    front3("bioshock") ➞ "biobiobio"

### Notes

Don't forget to `return` the result.

"""

def front3(text):
  if len(text) < 3:
    prefix = text
  else:
    prefix = text[:3]
  return prefix*3

