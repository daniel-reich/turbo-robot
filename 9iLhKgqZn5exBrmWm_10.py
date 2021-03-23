"""


Write a function that returns `True` if a string consists of **ascending or
ascending AND consecutive** numbers.

### Examples

    ascending("232425") ➞ True
    # Consecutive numbers 23, 24, 25
    
    ascending("2324256") ➞ False
    # No matter how this string is divided, the numbers are not consecutive.
    
    ascending("444445") ➞ True
    # Consecutive numbers 444 and 445.

### Notes

A **number** can consist of any number of digits, so long as the numbers are
adjacent to each other, and the string has at least two of them.

"""

def ascending(txt):
  for n_len in range(1, (int)(len(txt)/2)+1):
      if len(txt)%n_len != 0:
          continue
      prev = int(txt[:n_len])
      i = n_len
      has_asc = True
      while i+n_len < len(txt)+1:
          curr = int(txt[i:i+n_len])
          if curr - prev != 1:
              has_asc = False
              break
          i += n_len
          prev = curr
      if has_asc:
          return True
  return False

