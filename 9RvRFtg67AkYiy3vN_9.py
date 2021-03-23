"""


Create a **left rotation** and a **right rotation** function that returns all
the left rotations and right rotations of a string.

### Examples

    left_rotations("abc") ➞ ["abc", "bca", "cab"]
    
    right_rotations("abc") ➞ ["abc", "cab", "bca"]
    
    left_rotations("abcdef")
    ➞ ["abcdef", "bcdefa", "cdefab", "defabc", "efabcd", "fabcde"]
    
    right_rotations("abcdef")
    ➞ ["abcdef", "fabcde", "efabcd", "defabc", "cdefab", "bcdefa"]

### Notes

N/A

"""

def left_rotations(txt):
    r = [txt]
    new = txt
    for i in range(len(txt) - 1):
        new = new[1:] + new[0]
        r.append(new)
    return r
def right_rotations(txt):
    r = [txt]
    new = txt
    for i in range(len(txt) - 1):
        new = new[-1] + new[: - 1]
        r.append(new)
    return r

