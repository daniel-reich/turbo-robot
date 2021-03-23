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
  arr = [0]
  for i in range(1,len(txt)):
    if txt[i] != txt[i-1]:
      arr.append(i)
  arr.append(len(txt))
  if len(arr)%2 == 0: return False
  for i in range(1,len(arr),2):
    if arr[i] - arr[i-1] != arr[i+1] - arr[i]:
      return False
  return True

