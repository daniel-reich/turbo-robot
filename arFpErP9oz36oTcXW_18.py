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
  txt_split = txt.split(".")
  tag = txt_split[0]
  classes = ""
  for i in range(1,len(txt_split)):
    classes += txt_split[i]
    if i != len(txt_split) - 1:
      classes += " "
  
  return("<{} class='{}'></{}>".format(tag, classes, tag))

