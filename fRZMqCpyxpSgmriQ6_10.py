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
    lower = ''
    upper = ''
    number = ''
    for i in s:
        if i.isdigit():
            number += i
        elif i.islower():
            lower += i
        else:
            upper += i
    sort_nums = ''.join(sorted(number))
    sort_upper = ''.join(sorted(upper))
    sort_lower = ''.join(sorted(lower))
    sort_digits = sort_lower + sort_upper
    sort_digits = ''.join(sorted(sort_digits, key=lambda v: v.upper()))
    return sort_digits + sort_nums

