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

def negative_sum(chars):
    r, add = [], "-"
    while "-" in chars:
        s = chars.index("-")
        chars = chars[s:]
        s = 0
        while s + 1 < len(chars) and chars[s + 1].isnumeric(): 
            s += 1
        add = int(chars[: s + 1])
        r.append(add)
        add = "-"
        chars = chars[s + 1 :]   
    return sum(r)

