"""


Create a function that takes an array of three numbers and returns the **Least
Common Multiple** (LCM).

The LCM is the smallest positive number that is a multiple of two or more
numbers. In our case, we are dealing with three numbers.

  * Multiples of 3 are: 3, 6, 9, 12, and so on.
  * Multiples of 4 are: 4, 8,12, and so on.
  * Multiples of 12 are: 12, and so on.

Thus, the least common multiple of 3, 4, and 12 is 12.

### Examples

    lcm_three([5, 7, 13]) ➞ 455
    
    lcm_three([104, 105, 107]) ➞ 1168440
    
    lcm_three([19, 47, 43]) ➞ 38399

### Notes

N/A

"""

def lcm_three(num):
  m = max(num)
  lcm = 0
  wee = 0
  while lcm == 0:
    wee += m
    if wee % num[0] == 0 and wee % num[1] == 0 and wee % num[2] == 0:
      lcm = wee
  return lcm

