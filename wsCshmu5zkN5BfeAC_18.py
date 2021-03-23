"""


Create a function that takes a number `n` and checks if each digit is
divisible by the digit on its left. Return a boolean array depending on the
condition checks.

### Examples

    divisible_by_left(73312) ➞ [False, False, True, False, True]
    # no element left to 7 = False
    # 3/7 = False
    # 3/3 = True
    # 1/3 = False
    # 2/1 = True
    
    divisible_by_left(1) ➞ [False]
    
    divisible_by_left(635) ➞ [False, False, False]

### Notes

The array should always start with `False` as there is no digit to the left of
the first digit.

"""

def divisible_by_left(n):
  newlist = []
  first = str(n)
  for x in first:
    newlist += [int(x)]
  
  final = []
  length = len(newlist)
  while length > 0:
    if length == 1:
      final = [False] + final
      return final
    elif newlist[length-2] == 0:
      final = [False] + final
      length = length - 1
    elif newlist[length-1] % newlist[length-2] == 0:
      final = [True] + final
      length = length - 1
    else:
      final = [False] + final
      length = length - 1
