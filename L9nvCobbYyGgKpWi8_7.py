"""


Write two functions:

  1. `to_list()`, which converts a number to an integer list of its digits.
  2. `to_number()`, which converts a list of integers back to its number.

### Examples

    to_list(235) ➞ [2, 3, 5]
    
    to_list(0) ➞ [0]
    
    to_number([2, 3, 5]) ➞ 235
    
    to_number([0]) ➞ 0

### Notes

All test cases will be weakly positive numbers: `>= 0`

"""

def to_list(num):
  mylist = []
  str_num = str(num)
  for i in range (len(str_num)):
    mylist.append(int(str_num[i]))
  return mylist
  
def to_number(lst):
  mul = 0
  for i in range (len(lst)):
      mul = mul*10 + lst[i]
  return mul

