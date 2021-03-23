"""


Create a function that takes two integers, `num` and `n`, and returns an
integer which is divisible by `n` and is the closest to `num`. If there are
two numbers equidistant from `num` and divisible by `n`, select the larger
one.

### Examples

    round_number(33, 25) ➞ 25
    
    round_number(46, 7) ➞ 49
    
    round_number(133, 14) ➞ 140

### Notes

`n` will always be a positive number.

"""

def round_number(num, n):
  first = 0
  second = 0
  for i in reversed(range(num+1)):
    if i % n == 0:
      first = i
      break
  for i in range(num,num+n+1):
    if i % n == 0:
      second = i
      break
  return first if num - first < abs(num - second) else second

