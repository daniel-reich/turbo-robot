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
  def is_divisible_by(n):
    def divisible_by(num):
      return num % n == 0
    return divisible_by
  
  divisor = is_divisible_by(n)
  closest = []
  
  for number in range(num - n, num + n + 1):
    divisible = divisor(number)
    if divisible == True:
      closest.append(number)
  
  minim = min(closest)
  maxim = max(closest)
  
  if len(closest) != 2:
    return False, 'L19'
  
  mindif = num - minim
  maxdif = maxim - num
  
  if mindif > maxdif:
    return maxim
  elif mindif < maxdif:
    return minim
  else:
    return maxim

