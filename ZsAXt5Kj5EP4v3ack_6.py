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
  g = re.match(r'^(\w+)\>(\w+)\.(\w+)',txt)
  num = int(re.findall(r'\d+$',txt)[0])
  string = lambda x: '<{} class=\'{}\'></{}>'.format(g.group(2),g.group(3)+(txt.count('$')-1)*'0'+str(x),g.group(2))
  return '<{}>{}</{}>'.format(g.group(1),''.join(string(x) for x in range(1,num+1)),g.group(1))

