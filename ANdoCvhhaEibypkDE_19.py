"""


Create a function that returns the sum of the digits formed from the first and
last digits, all the way to the center of the number.

### Worked Example

    closing_in_sum(2520) ➞ 72
    
    # The first and last digits are 2 and 0.
    # 2 and 0 form 20.
    # The second and second to last digits are 5 and 2.
    # 5 and 2 form 52.
    
    # 20 + 52 = 72

### Examples

    closing_in_sum(121) ➞ 13
    # 11 + 2
    
    closing_in_sum(1039) ➞ 22
    # 19 + 3
    
    closing_in_sum(22225555) ➞ 100
    # 25 + 25 + 25 + 25

### Notes

  * If the number has an **odd** number of digits, simply add on the single-digit number in the center (see example #1).
  * Any number which is **zero-padded** counts as a single digit (see example #2).

"""

import math
def closing_in_sum(n):
  n = str(n)
  if int(len(n))%2 == 0:
    gb = [n[i] +n[-i-1] for i in range(int(len(n)/2))]
    return (sum([int(i) for i in gb]))
  else:
    bb = [n[i] +n[-i-1] for i in range(math.floor(int(len(n)/2)))]
    return (sum([int(i) for i in bb])) + int(n[len(n)//2])

