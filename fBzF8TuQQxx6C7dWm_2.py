"""


Create a function that will put the first argument, a character, between every
word in the second argument, a string.

### Examples

    add("R", "python is fun") ➞ "pythonRisRfun"
    
    add("#", "hello world!") ➞ "hello#world!"
    
    add("#", " ") ➞ "#"

### Notes

Make sure there are no spaces between words when returning the function.

"""

def add(char, txt):
#Per request of test 3, .join() will be used; .replace() would also work
  if txt==" ":
    return char
  return char.join(txt.split())

