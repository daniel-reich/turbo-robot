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
  output = [txt]
  rotstring = txt[1:]+txt[0]
  output.append(rotstring)
  while rotstring != txt:
    rotstring = rotstring[1:]+rotstring[0]
    output.append(rotstring)
  return output[:-1]
​
def right_rotations(txt):
  output = [txt]
  rotstring = txt[-1]+txt[:-1]
  output.append(rotstring)
  while rotstring != txt:
    rotstring = rotstring[-1]+rotstring[:-1]
    output.append(rotstring)
  return output[:-1]

