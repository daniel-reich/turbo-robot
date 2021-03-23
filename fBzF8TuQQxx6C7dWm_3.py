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
  new_txt = ''
  for i in txt:
    if i == ' ':
      i = char
    new_txt += i
  return new_txt

