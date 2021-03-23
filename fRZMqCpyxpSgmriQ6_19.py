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
  alpha = sorted(set([i.lower() for i in s if i.isalpha()]))
  lower = sorted([i for i in s if i.isalpha() and i.islower()])
  upper = sorted([i for i in s if i.isalpha() and i.isupper()])
  digit = sorted([i for i in s if i.isdigit()])
  lst = []
  for i in alpha:
    if i in lower:
      lst.append(i)
    if i.upper() in upper:
      lst.append(i.upper())
  return ''.join(lst+digit)

