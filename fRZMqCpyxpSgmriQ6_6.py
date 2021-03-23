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

import string as s 
def sorting(t):
  p3=list(zip(s.ascii_lowercase,s.ascii_uppercase))
  p4=[p3[i][a] for i in range(len(p3)) for a in range(len(p3[i]))]+list(s.digits)
  return ''.join(sorted(t,key=p4.index))

