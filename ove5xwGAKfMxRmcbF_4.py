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

match = lambda s1, s2: s1.lower() == s2.lower()

