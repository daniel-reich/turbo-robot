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
  i = 1
  while i < len(txt):
    if not len(txt)%i:
      temp = [int(txt[j:j+i]) for j in range(0,len(txt),i)]
      if all(temp[k] == temp[k-1]+1 for k in range(1,len(temp))):
        return True
    i += 1
  return False

