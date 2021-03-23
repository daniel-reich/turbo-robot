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
  result = []
  a = len(txt)
  for i in range(a):
    result.append(txt[i:]+txt[0:i])
  return result
  
def right_rotations(txt):
  result = []
  a = len(txt)
  for i in range(a):
    if i != 0:
      result.append(txt[(a-i)%a:]+txt[0:a-i])
    else:
      result.append(txt[(a-i)%a:])
  return result

