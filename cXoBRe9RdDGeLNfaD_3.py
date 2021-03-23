"""


You will be given a simple string expression representing an addition or
subtraction in 8-bit 2's complement arithmetic. Write a function that returns
the result in base 10 followed by a binary representation. If any of the
values are outside the range of 8-bit 2's complement, return `"Overflow"`.

### Examples

    eight_bit("3 + 12") ➞ (15, "11 + 1100 = 1111")
    
    eight_bit("3 - 12") ➞ (-9, "11 - 1100 = 11110111")
    
    eight_bit(-18 - 6) ➞ (-24, "11101110 - 110 = 11101000")
    
    eight_bit(65 + 70) ➞ "Overflow"
    
    eight_bit(-127 + 127) ➞ (0, "10000001 + 1111111 = 0")

### Notes

Numbers in 8-bit 2's complement notation can range from -128 to 127. The
eighth (leftmost) bit signifies a negative number. See **Resources** for
details.

"""

def eight_bit(x):
  res = eval(x)
  x = x.split()
  x = [int(x[0]), x[1], int(x[2]), '=', res]
  for i in range(0,5,2):
    if not -128 <= x[i] < 128:
      return 'Overflow'
    if x[i] >= 0:
      x[i] = '{:b}'.format(x[i])
    else:
      x[i] = '1' + '{:07b}'.format(x[i]+128)
  return (res,' '.join(x))

