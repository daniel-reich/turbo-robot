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
  ones = [i for i in txt.split('0') if i != '']
  zeroes = [i for i in txt.split('1') if i != '']
  if len(ones) != len(zeroes):
    return False
  for i in range(len(ones)):
    if len(ones[i]) != len(zeroes[i]): 
      return False
  return True

