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
    number = sum(1 for ch in txt if ch == "$")
    parent, child, class_name, times = "".join(
        "." if ch in ">*" else "" if ch == "$" else ch for ch in txt).split(".")
    return "<{}>".format(parent) + "".join("<{} class='{}{}'></{}>".format(child, class_name, "0"*(number - 1) + str(n), child) for n in range(1, int(times) + 1)) + "</{}>".format(parent)

