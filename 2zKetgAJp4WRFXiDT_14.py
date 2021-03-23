"""


Create a function that takes a number `num` and returns its length.

### Examples

    number_length(10) ➞ 2
    
    number_length(5000) ➞ 4
    
    number_length(0) ➞ 1

### Notes

 **The use of the len() function is prohibited.**

"""

def number_length(num):
  
  if (num < 10):
    return 1
  else:
    Total = 0
    Power = 0
    Addition = 9 * (10 ** Power)
    Length = 0
    
    while (Total < num):
      Total += Addition
      Length += 1
      Power += 1
      Addition = 9 * (10 ** Power)
      
    return Length

