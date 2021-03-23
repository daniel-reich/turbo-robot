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

num_split=lambda n:[int(x)*10**i*(1,-1)[n<0]for i,x in enumerate(str(n)[::-1].strip('-'))][::-1]

