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

def match(str1, str2):
    if str1.lower() == str2.lower():
        return True
    else:
        return False

