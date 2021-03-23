"""


Write a function that returns `True` if every consecutive sequence of **ones**
is followed by a consecutive sequence of **zeroes** of the same length.

### Examples

    same_length("110011100010") ➞ True
    
    same_length("101010110") ➞ False
    
    same_length("111100001100") ➞ True
    
    same_length("111") ➞ False

### Notes

N/A

"""

def same_length(txt):
    count = 0
    increasing = True
    for i in txt:
        if i == "1":
            if not increasing:
                if count != 0:
                    return False
                increasing = True
            count += 1
        elif i == "0":
            increasing = False
            count -= 1
    if count == 0:
        return True
    return False

