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
    a='';b='';c=''
    for i in s:
        if i.isalpha() and i.islower():
           a=a+i
        elif i.isalpha() and i.isupper():
           b=b+i
        else:
           c=c+i
        
    r=''.join(sorted(a,key=lambda x: (not x.islower(),x))+sorted(b,key=lambda x: (not x.isupper(),x)))
    return ''.join(sorted(r, key=str.casefold,))+''.join(sorted(c))

