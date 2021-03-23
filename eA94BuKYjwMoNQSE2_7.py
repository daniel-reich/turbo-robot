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
  result = []
  lst = txt.split(" ")
  print(lst)
  ops = []
  nums = []
  for l in lst:
    if l in "<>":
      ops.append(l)
    else:
      nums.append(int(l))
  for i in range(len(ops)):
    print(result)
    print(nums[i], nums[i+1])
    print(lst[i] < lst[i+1])
    print(7<11)
    if ops[i] == "<":
      if nums[i] < nums[i+1]:
        print("hi")
        result.append(True)
      else:
        print("hi2")
        result.append(False)
    elif ops[i] == ">":
      if nums[i] > nums[i+1]:
        result.append(True)
      else:
        result.append(False)
  print(result)
  if result[0] == True and len(set(result)) == 1:
    return True
  else:
    return False

