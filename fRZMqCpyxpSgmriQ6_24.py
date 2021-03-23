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
  l = "".join(filter(lambda x: x.isalpha(), sorted(sorted(s, reverse=True), key=str.lower)))
  n = "".join(i for i in sorted(s) if i.isdigit())
  return l + n

