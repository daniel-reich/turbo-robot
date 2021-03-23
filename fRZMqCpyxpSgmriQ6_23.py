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

import re
​
def sorting(s):
  numbers = re.findall(r'\d',s)
  letters = re.findall(r'\D',s)
  letters.sort(key = lambda x: ord(x.lower()))
  letters = ''.join(letters)
  numbers.sort()
  lst = list(map(lambda x: x.upper() + x.lower(), 'abcdefghijklmnopqrstuvwxyz'))
  for item in lst:
    letters = letters.replace(item,item[::-1])
  return ''.join(letters) + ''.join(numbers)

