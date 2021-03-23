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
  txt = txt.split('>')
  final = '<{}>'.format(txt[0])
  tag = "<{0} class='{1}$'></{0}>".format(txt[1].split('.')[0],txt[1].split('.')[1].split('$')[0])
  tag = tag.replace('$','{}')
  for i in range(1,int(txt[1][-1])+1):
    final+=tag.format('0'*(txt[1].count('$')-1)+str(i))
  return final+'</{}>'.format(txt[0])

