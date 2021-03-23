"""


Create a function which adds spaces before every capital in a word.
Uncapitalize the whole string afterwards.

### Examples

    cap_space("helloWorld") ➞ "hello world"
    
    cap_space("iLoveMyTeapot") ➞ "i love my teapot"
    
    cap_space("stayIndoors") ➞ "stay indoors"

### Notes

The first letter will stay uncapitalized.

"""

def cap_space(txt):
​
    newtxt=""
    for i in txt:
        if i==i.upper():
             newtxt+=" "
        newtxt += i
    return newtxt.lower()
​
print(cap_space("helloWorld"))

