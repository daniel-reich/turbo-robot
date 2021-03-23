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
  n=1
  while n<len(txt)/2+1:
    chunks = [int(txt[i:i+n]) for i in range(0,len(txt),n)]
    if all(chunks[j]-chunks[j-1]==1 for j in range(1,len(chunks))):
      return True
    n+=1
  return False

