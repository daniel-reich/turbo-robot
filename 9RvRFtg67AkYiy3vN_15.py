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

def left_rotations(str1):
  lk=[]
  lk.append(str1)
  for i in range(1,len(str1)):
    lk.append(str1[i:]+str1[:i])
  return lk
def right_rotations(txt):
  rk=[]
  vr=left_rotations(txt)
  fst=vr[0]
  rk.append(fst)
  rk.extend(vr[::-1][:-1])
  return rk

