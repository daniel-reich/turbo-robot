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
  n = int(text[-1])
  a = '<' + text[:-2] + '>'
  b = '</' + text[:-2] + '>'
  c = a+b
  return n*c

