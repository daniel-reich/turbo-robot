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
  res = [False]
  str_n = str(n)
  for i in range(1,len(str_n)):
    if str_n[i - 1] == '0':
      res.append(False)
    else:
      res.append(int(str_n[i]) % int(str_n[i - 1]) == 0)
  return res

