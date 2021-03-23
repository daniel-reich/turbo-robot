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
   b,c='',''
   a=sorted(s, key=lambda v: (v.lower(), v[0].isupper()))
   for i in  a:
     if ord(i)>=48 and ord(i)<=57:
        b=b+i
     else:
        c=c+i
   d=c+b
   return(d)

