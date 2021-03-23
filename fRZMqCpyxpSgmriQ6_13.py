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

import string
def sorting(s):
    return ''.join([i[1] for i in sorted([(([sub[item] for item in range(len(string.ascii_lowercase)) for sub in [string.ascii_lowercase, string.ascii_uppercase]] + list(string.digits)).index(i), i) for i in s], key = lambda k: k[0])])

