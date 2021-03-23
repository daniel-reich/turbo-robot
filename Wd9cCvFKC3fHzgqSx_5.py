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
  if abs(num) < 10:
    return [num]
  if num < 0:
    k = -1
  else:
    k = 1
  return list(map(lambda x: k * 10 * x, num_split(abs(num) // 10))) + [k * (abs(num) % 10)]

