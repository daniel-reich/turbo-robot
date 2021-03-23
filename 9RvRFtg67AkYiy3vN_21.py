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
    a=list(txt)
    b=[]
    b.append("".join(a))
    for i in range(len(a)-1):
        a.append(a.pop(0))
        b.append("".join(a))
    return(b)
  
​
def right_rotations(txt):
    a=list(txt)
    b=[]
    b.append("".join(a))
    for i in range(len(a)-1):
        a.insert(0,a.pop())
        b.append("".join(a))
    return(b)

