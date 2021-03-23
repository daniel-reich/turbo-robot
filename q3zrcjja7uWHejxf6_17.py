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
    result = []
    for i in range(len(chars)):
        if chars[i] == "-":
            j = 1
            while chars[i + j].isdigit():
                   if i + j == len(chars) - 1:
                       j += 1
                       break
                   else:
                       j += 1
            result.append(chars[i + 1: i + j])
    return sum(int(num) for num in result) * -1

