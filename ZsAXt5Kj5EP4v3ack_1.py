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

def secret(s):
  a = s.split('>')[0]
  b = s.split('>')[1].split('.')[0]
  c = s.split('.')[1].split('*')[0]
  d = int(s.split('*')[1])
  ret = '<'+a+'>'
  for i in range(1,d+1):
    ret+='<'+b+" class='"+c.split('$')[0]+('0'*(c.count('$')-1))+str(i)+"'></"+b+'>'
  ret+='</'+a+'>'
  return ret

