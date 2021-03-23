"""


Write a function that returns `True` if every consecutive sequence of **ones**
is followed by a consecutive sequence of **zeroes** of the same length.

### Examples

    same_length("110011100010") ➞ True
    
    same_length("101010110") ➞ False
    
    same_length("111100001100") ➞ True
    
    same_length("111") ➞ False

### Notes

N/A

"""

def same_length(txt):
  if len(txt) % 2 or txt[-1] == "1":
    return False
  ones = 0
  counter = 0
  while counter >= len(txt):
    if txt[counter] == "1":
      ones += 1
    elif "1" in txt[counter:counter + ones]:
      return False
    else:
      counter += ones
      ones = 0
    counter += 1
  return True

