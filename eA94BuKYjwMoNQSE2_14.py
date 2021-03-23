"""


Create a function that returns `True` if a given inequality expression is
correct and `False` otherwise.

### Examples

    correct_signs("3 < 7 < 11") ➞ True
    
    correct_signs("13 > 44 > 33 > 1") ➞ False
    
    correct_signs("1 < 2 < 6 < 9 > 3") ➞ True

### Notes

N/A

"""

def correct_signs(txt):
​
  tmp = txt.split()
  nums = tmp[0::2]
  syms = tmp[1::2]
  
  for i in range(len(nums) - 1):
    if (int(nums[i]) < int(nums[i+1]) and syms[i] == "<") or (int(nums[i]) > int(nums[i+1]) and syms[i] == ">"):
      return True
    else:
      return False

