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
  for i in range(1, len(txt)):
    if len(txt)/i == float(len(txt)//i):
      passed = True
      for j in range(1, len(txt)//i):
        if not int(txt[i*j:i*(j+1)]) == int(txt[i*(j-1):i*j]) + 1:
          passed = False
          break
      if passed:
        return True
  return False

