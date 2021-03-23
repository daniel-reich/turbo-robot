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

import re
def secret(txt):
  m = re.fullmatch(r'(\w+)>(\w+)\.(\w+)(\$+)\*(\d+)', txt)
  outer_tag, inner_tag, class_name, layout, count = m.groups()
  layout = len(layout)
  count = int(count)
  inner_format = "<{tag_name} class='{prefix}{i:0>{width}}'></{tag_name}>"
  out = []
  out.append("<{}>".format(outer_tag))
  for idx in range(1, count + 1):
    out.append(inner_format.format(tag_name=inner_tag, prefix=class_name, width=layout, i=idx))
  out.append("</{}>".format(outer_tag))
  return ''.join(out)

