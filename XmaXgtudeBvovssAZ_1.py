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

from math import pi,sin,atan
def red_area(r):
    ang=pi-2*atan(.5)
    return round(r*r*pi/4-r*r*(ang-sin(ang))/2,3)

