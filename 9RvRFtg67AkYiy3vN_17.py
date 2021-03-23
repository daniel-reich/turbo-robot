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

from collections import deque
def left_rotations(txt):
    DQ = deque(txt)
    L = []
    L.append(''.join(DQ))
    for i in range(len(txt)-1):
        DQ.rotate(-1)
        L.append(''.join(DQ))
    print(L)
    return L
​
def right_rotations(txt):
    DQ = deque(txt)
    L = []
    L.append(''.join(DQ))
    for i in range(len(txt)-1):
        DQ.rotate(1)
        L.append(''.join(DQ))
    print(L)
    return L

