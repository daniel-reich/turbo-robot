"""


Create a function based on the input and output. Look at the examples, there
is a pattern.

### Examples

    secret("div*2") ➞ "<div></div><div></div>"
    
    secret("p*1") ➞ "<p></p>"
    
    secret("li*3") ➞ "<li></li><li></li><li></li>"

### Notes

Input is a string.

"""

def secret(text):
  st = text.split("*")
  n = int(st[1])
  r = ""
  for i in range(n):
    r += "<{0}></{0}>".format(st[0])
  return r

