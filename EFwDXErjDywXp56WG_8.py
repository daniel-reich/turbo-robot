"""


Create a function that takes a string and returns `True` or `False`, depending
on whether the characters are in order or not.

### Examples

    is_in_order("abc") ➞ True
    
    is_in_order("edabit") ➞ False
    
    is_in_order("123") ➞ True
    
    is_in_order("xyzz") ➞ True

### Notes

You don't have to handle empty strings.

"""

def is_in_order(txt):
    y=list(txt)
    h=[i for i in txt]
    h.sort()
    return y==h

