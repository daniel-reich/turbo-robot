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
  text = text.split('*')
  return ''.join(['<' + text[0] + '></' + text[0] + '>' for i in range(int(text[1]))])

