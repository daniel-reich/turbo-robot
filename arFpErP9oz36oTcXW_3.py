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

import re
def secret(txt):
  return re.sub("(\w+)(?= ) (.*)", r"<\1 class='\2'></\1>", txt.replace('.',' '))

