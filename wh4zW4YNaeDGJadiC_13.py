"""


You are given two numbers, `a` and `b`. Write a function which uses an
expression to return the expected output. I am not going to tell you what the
expression is because that will spoil the fun! :)

### Examples

    crazyfunction(10, 20) ➞ 30
    
    crazyfunction(17, 35) ➞ 50
    
    crazyfunction(61, 233) ➞ 212

### Notes

Hint: Notice the tags?

"""

def crazyfunction(a, b):
    aa = bin(a)[2:]
    bb = bin(b)[2:]
​
    bs = int(aa,2) ^ int(bb,2)
    return bs

