"""


Create a function that takes a list of numbers and returns the _greatest
common factor_ of those numbers.

### Examples

    gcd([84, 70, 42, 56]) ➞ 14
    
    gcd([19, 38, 76, 133]) ➞ 19
    
    gcd([120, 300, 95, 425, 625]) ➞ 5

### Notes

The GCD is the largest factor that divides all numbers in the list.

"""

def gcd(lst):
  minnum = min(lst)
  newlist = []
  factor = False
  count = 0
  for i in range(1,minnum+1):
    for eachnumber in lst:
      if eachnumber % i == 0:
        count += 1
        continue
    if count == len(lst):
      newlist.append(i)
      count = 0
    else:
      count = 0
  return max(newlist)

