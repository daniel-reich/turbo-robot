"""


Create a function that takes a string containing integers as well as other
characters and return the sum of the negative integers only.

### Examples

    negative_sum("-12 13%14&-11") ➞ -23
    # -12 + -11 = -23
    
    negative_sum("22 13%14&-11-22 13 12") ➞ -33
    # -11 + -22 = -33

### Notes

There is at least one negative integer.

"""

def negative_sum(s):
    tot = 0
    beg = 0
    ln = len(s)
    while True:
        try:
            i = s.index('-', beg)
            n = s[i]
            for x in s[i+1:]:
                if x.isdigit():
                    n += x
                else:
                    break
            tot += int(n)
            beg = i + 1
        except:
            break
    return tot

