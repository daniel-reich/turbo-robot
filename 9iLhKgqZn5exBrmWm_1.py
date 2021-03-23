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

def ascending(t):
  l=len(t)
  for i in range(l,1,-1):
    k=[int(t[j:j+l//i])for j in range(0,l,l//i)]
    if k and all(y-x==1 for x,y in zip(k,k[1:])):return 1
  return 0

