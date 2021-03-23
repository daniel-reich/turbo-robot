"""


This problem went viral in China, spreading on Weibo. The problem is to solve
for the area shown in red between the semicircle and the rectangle’s diagonal.

Create a function that takes a number `r` as an the length of the side and
returns the area rounded to the nearest thousandth.

![The shaded part](https://edabit-
challenges.s3.amazonaws.com/solve_red_area.png)

### Examples

    redArea(0) ➞ 0
    
    redArea(4) ➞ 1.252
    
    redArea(25) ➞ 48.906

### Notes

The input `r` is always a valid number.

"""

import math
​
ref = -4 * math.pi + 16 * math.atan(0.5) + 6.4
​
def red_area(r):
  return 0 if r == 0 else round(ref * (r / 4.)**2, 3)

