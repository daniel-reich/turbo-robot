"""


Create a function that takes a range of numbers and returns the sum of each
digit from `start` to `stop`.

### Examples

    digits_sum(1, 10) ➞ 46
    # total numbers in the range are = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # sum of each digits is = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 = 46
    
    digits_sum(1, 20) ➞ 102
    
    digits_sum(1, 100) ➞ 901

### Notes

`start` and `stop` are inclusive in the range.

"""

import math
​
def digits_sum(start, stop):
  return sum_of_digits(stop) - sum_of_digits(start - 1)
​
def sum_of_digits(n):
  if n < 10:
    return (n * (n +1)) / 2
  d = int(math.log10(n))
  lst = [0] * (d + 1)
  lst[1] = 45
  for i in range(2, d + 1):
    lst[i] = lst[i - 1] * 10 + 45 * int(math.ceil(math.pow(10, i - 1)))
  p = int(math.ceil(math.pow(10, d)))
  msd = n // p
  return int(msd * lst[d] + (msd * (msd - 1) // 2) * p +
          msd * (1 + n % p) + sum_of_digits(n % p))

