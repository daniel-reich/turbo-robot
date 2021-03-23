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
  txt = txt.replace(".", " ")
  txt = txt.split()
  
  txt_middle = " ".join(txt[1:])
  tag_start = "<" + txt[0] + " "
  tag_end = "></" + txt[0] + ">"  
  class_middle = "class=" + "'" + txt_middle + "'"
  
  return tag_start + class_middle  + tag_end

