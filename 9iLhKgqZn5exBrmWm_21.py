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

def wrap(s, w):
    return [s[i:i + w] for i in range(0, len(s), w)]
​
​
def ascending(txt):
  st = 1
  i=0
  for j in range(len(txt)):
    X = wrap(txt, j+1)
    fo =0
    for i in range(len(X)-1):
      if int(X[i+1]) == int(X[i]) +1:
        fo = 1
      else:
        fo =0
        break
    if fo:
      return True
  return False

