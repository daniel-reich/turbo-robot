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

from re import match
def secret(s):
    m = match(r"(\w+)>(\w+)\.(\w+)([$]+)\*(\d)", s)
    return ("<{0}>{1}</{0}>"
            .format(m.group(1),
                    "".join("<{0} class=\'{1}{2}{3}\'></{0}>"
                            .format(m.group(2), m.group(3),
                                    "0" * (len(m.group(4)) - 1), i)
                            for i in range(1, int(m.group(5)) + 1))))

