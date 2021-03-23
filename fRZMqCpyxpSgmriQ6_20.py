"""
Create a function that takes a string consisting of **lowercase letters** ,
**uppercase letters** and **numbers** and returns the string sorted in the
same way as the examples below.

### Examples

    sorting("eA2a1E") ➞ "aAeE12"
    // Don't repeat letters.
    
    sorting("Re4r") ➞ "erR4"
    
    sorting("6jnM31Q") ➞ "jMnQ136"
    
    sorting("846ZIbo") ➞ "bIoZ468"

### Notes

Don't repeat letters (numbers can be repeated).

"""

def sorting(s):
    import string
    lst = ''
    order = zip(string.ascii_lowercase, string.ascii_uppercase)
    for (l,u) in list(order):
        if l in s:
            lst += l
        if u in s:
            lst += u
    for digit in string.digits:
        if digit in s:
            lst += digit
    return lst

