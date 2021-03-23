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
  max_div = 1
  for i in range(2, min(lst)+1):
    not_ok = True
    for j in lst:
      if j % i != 0:
        not_ok = False
        break
    if not_ok:
      max_div = i
  return max_div

