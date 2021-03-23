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
  x = text.split('*')
  return ''.join('<' + x[0] + '>' if i % 2 == 0 else "</" + x[0] + '>' for i in range(int(x[1])*2))

