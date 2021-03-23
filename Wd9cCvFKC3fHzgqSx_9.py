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
    r = []
    if num < 0:
        neg = "-"
    else:
        neg = ""
    num = abs(num)
    for i in range(len(str(num))):
        add = neg + str(num)[i] + "0" * (len(str(num)) - i - 1)
        r.append(int(add))
    return r

