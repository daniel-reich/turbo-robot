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
  
  consecuatives = []
  used = []
  
  for n in range(0, len(txt)):
    if n not in used:
      item = txt[n]
      t = item
      c = 0
      start = n
      n += 1
      while n < len(txt) and txt[n] == item and c < 1000:
        t += item
        n += 1
        c += 1
      for num in range(start, n):
        used.append(num)
      consecuatives.append(t)
  
  for n in range(0, len(consecuatives), 2):
    try:
      if len(consecuatives[n]) != len(consecuatives[n+1]):
        return False
    except IndexError:
      return False
  return True

