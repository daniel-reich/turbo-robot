"""


You are given one input: A list containing eight 1's and/or 0's. Write a
function that takes an `8 bit` binary number and convert it to decimal.

### Examples

    binary_to_decimal([1, 1, 1, 1, 1, 1, 1, 1]) ➞ 255
    
    binary_to_decimal([0, 0, 0, 0, 0, 0, 0, 0]) ➞ 0
    
    binary_to_decimal([1, 0, 1, 1, 1, 1, 0, 0]) ➞ 188

### Notes

Return an integer.

"""

def binary_to_decimal(binary):
  sum_integer = 0
  power = (len(binary) - 1)
  i = 0
  while power >= 0 and i <= (len(binary) - 1):
    if binary[i] == 1:
      sum_integer += (2 ** power)
      power -= 1
      i += 1
    else:
      sum_integer += 0
      power -= 1
      i += 1
  return sum_integer

