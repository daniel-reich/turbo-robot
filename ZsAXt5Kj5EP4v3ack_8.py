"""


Create a function based on the input and output. Look at the examples, there
is a pattern.

### Examples

    secret("div>p.a$$*2") ➞ `<div><p class="a01"></p><p class="a02"></p></div>`
    # Only whitespace in the entire string ===  One whitespace before each class. Total " " === 2
    
    secret("ul>li.b$*3") ➞ `<ul><li class="b1"></li><li class="b2"></li><li class="b3"></li></ul>`
    # Only whitespace in the entire string === One whitespace before each class. Total " " === 3
    
    secret("p>h1.c$$$*2") ➞ `<p><h1 class="c001"></h1><h1 class="c002"></h1></p>`
    # Only whitespace in the entire string === One whitespace before each class. Total " " === 2

### Notes

Input is a string.

"""

def secret(txt):
  import collections
  digits = collections.Counter(txt)["$"]
  txt_split = [txt.split(">")[0]]
  txt_split.append(txt.split(">")[1].split(".")[0])
  txt_split.append(txt.split(".")[1].split("$")[0])
  txt_split.append(txt.split("*")[1])
  first_tag_name = txt_split[0]
  repeat_tag_name = txt_split[1]
  class_lead_letter = txt_split[2]
  repeats = int(txt_split[3])
  output = "<"+first_tag_name+">"
  closing_tag = "<"+"/"+repeat_tag_name+">"
  for i in range(1,repeats+1):
    output += "<" + repeat_tag_name + " class='" + class_lead_letter + "0"*(digits-len(str(i))) + str(i) + "'>" + closing_tag
  output += "<"+"/"+first_tag_name+">"
  return output

