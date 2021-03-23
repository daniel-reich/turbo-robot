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
  left_lst = []
  i = 0
  while i < len(txt):
    new_txt = txt[i:] + txt[:i]
    left_lst.append(new_txt)
    i += 1
  return left_lst
​
def right_rotations(txt):
  right_lst = []
  i = 0
  while i < len(txt):
    new_txt = txt[-i:] + txt[:-i]
    right_lst.append(new_txt)
    i += 1
  return right_lst

