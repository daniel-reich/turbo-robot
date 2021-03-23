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
  f,res = [1,-1][num < 0],[]
  num = abs(num)
  while num:
    num,r = divmod(num,10)
    res = [r*f]+res
    f *= 10
  return res

