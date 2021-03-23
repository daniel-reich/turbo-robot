"""


Create a function that takes a number `num` and returns each place value in
the number.

### Examples

    num_split(39) ➞ [30, 9]
    
    num_split(-434) ➞ [-400, -30, -4]
    
    num_split(100) ➞ [100, 0, 0]

### Notes

N/A

"""

def num_split(num):
  lst = []
  mlt = 1
  sign = 1
  # store the sign of num
  if num < 0:
    sign *= -1
    num *= sign
  # get the power of num
  while num // mlt >= 10:
    mlt *= 10
  # divide the number by mlt
  while mlt >= 1:
    lst.append((num // mlt) * mlt * sign)
    num -= (num // mlt ) * mlt
    mlt //= 10
  return lst

