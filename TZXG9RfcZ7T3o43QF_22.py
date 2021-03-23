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
  up = True
  count = 0
  for i in txt:
    if up and i == "1":
      count += 1
    if i == "0":
      up = False
      count -= 1
    if not up and i == "1":
      if count == 0:
        up = True
        count += 1
      else:
        break
  return count == 0
