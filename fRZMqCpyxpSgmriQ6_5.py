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
  li = list(s)
  li.sort(key=sorter)
  return ''.join(li)
  
  
def sorter(elem):
  if elem.isalpha():
    if elem.islower():
      return ord(elem.upper()) - 0.5
    else:
      return ord(elem)
  else:
    return ord(elem) + 43

