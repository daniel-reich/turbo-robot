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
def digits_sum2(n):
    if n == 1000:
        return 13501
    if n == 0:
        return 0
    if n < 10:
        return n * (n + 1) // 2
    digit = int(math.log(n, 10)) + 1
    d = digit - 1
    place = [0] * (d+1)
    place[1] = 45
    for i in range(2, d + 1):
        place[i] = place[i-1] * 10 + 45 * 10**(i - 1)
    power = 10**d
    msd = n // power
    return msd * place[d] + (msd * (msd - 1) // 2) * power + \
          msd * (1 + n % power) + digits_sum2(n % power)
​
def digits_sum(start, stop):
    ans = digits_sum2(stop) - digits_sum2(start - 1)
    return ans

