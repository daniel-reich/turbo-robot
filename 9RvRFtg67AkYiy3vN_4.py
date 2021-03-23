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
  k = [txt]
  for i in txt[:-1]:
    j = txt[1:] + txt[0]
    txt = j
    k.append(j)
  return k
    
def right_rotations(txt):
  k = [txt]
  for i in txt[:-1]:
    j = txt[-1] + txt[:-1]
    txt = j
    k.append(j)
  return k

