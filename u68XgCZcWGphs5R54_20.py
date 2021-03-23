"""


Create a function that takes a number and return a list of three numbers: half
of the number, quarter of the number and an eighth of the number.

### Examples

    half_quarter_eighth(6) ➞ [3, 1.5, 0.75]
    
    half_quarter_eighth(22) ➞ [11, 5.5, 2.75]
    
    half_quarter_eighth(25) ➞ [12.5, 6.25, 3.125]

### Notes

The order of the list is: half, quarter, eighth.

"""

def half_quarter_eighth(n):
 a = n/2
 b = n/4
 c = n/8
 thisl = list((a, b, c))
 return thisl

