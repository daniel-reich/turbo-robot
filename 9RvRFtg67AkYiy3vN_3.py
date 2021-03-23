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
  count = 1
  rotated_lst = []
  rotated_lst.append(txt)
  while count < len(txt):
    txt = txt[1:] + txt[0]
    rotated_lst.append(txt)
    count += 1
  return rotated_lst
​
def right_rotations(txt):
  count = 1
  rotated_lst = []
  rotated_lst.append(txt)
  while count < len(txt):
    txt = txt[-1] + txt[:-1]
    rotated_lst.append(txt)
    count += 1
  return rotated_lst

