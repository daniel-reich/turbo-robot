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

from re import sub
def secret(str):
  res = ''
  [a, b] = str.split('>')
  [c, d] = b.split('.')
  [e, f] = d.split('*')
  g = sub(r'[^a-z]', '', e)
  l = len(e) - len(g) - 1
  for i in range(1, int(f) + 1):
    res += "<{0} class='{1}{2}{3}'></{0}>".format(c, g, '0'*l, i)
  return "<{0}>{1}</{0}>".format(a, res)

