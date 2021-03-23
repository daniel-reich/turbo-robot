"""


Write a function that validates whether two strings are identical. Make it
case insensitive.

### Examples

    match("hello", "hELLo") ➞ True
    
    match("motive", "emotive") ➞ False
    
    match("venom", "VENOM") ➞ True
    
    match("mask", "mAskinG") ➞ False

### Notes

N/A

"""

match=lambda a,b:a.lower()==b.lower()

