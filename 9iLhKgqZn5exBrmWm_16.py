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
  print(txt)
  for i in range(1,len(txt)//2+1):
    temp = []
    for x in range(0,len(txt),i):
      temp.append(int(txt[x:x+i]))
    print(temp)
    if check(temp):
      return True
  return False
​
def check(lst):
  for i in range(1,len(lst)):
    if lst[i] != lst[i-1]+1:
      return False
  return True

