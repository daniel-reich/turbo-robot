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
  binary.reverse()
  sum=0
  for i in range(len(binary)):
    sum=sum+binary[i]*(2**i)
  return sum

