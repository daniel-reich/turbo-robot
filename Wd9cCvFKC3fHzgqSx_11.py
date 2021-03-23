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

def num_split(num):
    l = list(str(abs(num)))
    for i,v in enumerate(l):
        if num>0:l[i]=eval(str(v) + "0"*(len(l)-i-1))
        else: l[i]=eval(str(v) + "0"*(len(l)-i-1))*(-1)
    return l

