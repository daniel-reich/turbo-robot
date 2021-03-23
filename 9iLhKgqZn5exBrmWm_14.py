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

from functools import reduce
​
def ascending(txt):
  counter = 1
​
  while(counter <= (len(txt)//2)):
    lst = [int(item) for item in create_list(txt, counter)]
    results = []
​
    for i in range(0, len(lst)):
      if(i+2 <= len(lst)):
        results.append(reduce(lambda a, b: True if ((a+1) == b) else False, lst[i:i+2]))
​
    if(all(results)):
      return True
    else:
      counter += 1
  return False
def create_list(lst, n):
  result = []
​
  for i in range(0, len(lst), n):
    result.append(lst[i:i+n])
​
  return result

