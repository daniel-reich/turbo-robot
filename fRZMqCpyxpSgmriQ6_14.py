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
​
def sorting(s):
  init = sorted(s)
  numbers = []
  no_digit = []
​
  # store numbers
  for i in init:
    if i.isdigit():
      numbers.extend(i)
​
  # remove numbers from original string
  for i in init:
    if not i.isdigit():
      no_digit.extend(i)
​
  first_sort = sorted(no_digit, key=string.ascii_letters.index)
  final = sorted(first_sort, key=str.lower)
​
  # makes lists to string
  digit = "".join(numbers)
  new_s = "".join(final)
  
  return new_s+digit

