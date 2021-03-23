"""


Create a function based on the input and output. Look at the examples, there
is a pattern.

### Examples

    secret("p.one.two.three") ➞ "<p class='one two three'></p>"
    
    secret("p.one") ➞ "<p class='one'></p>"
    
    secret("p.four.five") ➞ "<p class='four five'></p>"

### Notes

Input is a string.

"""

def secret(txt):
​
  words = txt.split(".")
  result = "<"+words[0]+" class='"
  for i in range(1, len(words)):
    result += words[i]+" "
  result = result.rstrip()
  result += "'></"+words[0]+">"
  return result

