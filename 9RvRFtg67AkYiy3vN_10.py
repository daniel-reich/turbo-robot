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

def left_rotations(st):
    return [st[i:] + st[:i] for i in range(len(st))]
  
​
def right_rotations(st):
    l = []
    for i in range(len(st)):
        l.append(st)
        st = st[-1] + st[:-1]
    return l

