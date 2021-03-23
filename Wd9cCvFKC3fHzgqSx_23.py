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
  ret = []
  neg = num//abs(num)
  num = str(abs(num))[::-1]
  for i in range(len(num)):
    ret.append(int(num[i])*(10**i)*neg)
  return ret[::-1]

