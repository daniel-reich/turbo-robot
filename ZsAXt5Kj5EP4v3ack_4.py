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
    level1 = txt.split('>')[0]
    txt = ''.join(txt.split('>')[1:])
    level2 = txt.split('.')[0]
    txt = ''.join(txt.split('.')[1:])
    base = txt.split('$')[0]
    n = txt.count('$')
    classes = int(txt.split('*')[1])
    ans = "<" + level1 + ">"
    for i in range(1, classes + 1):
        ans += "<" + level2 + " class='" + base + str(i).zfill(n) + "'></" + level2 + ">"
    ans += "</" + level1 + ">"
    return ans

