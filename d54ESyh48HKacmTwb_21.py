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

def find_gcd(x, y):
  while(y):
    x, y = y, x % y
  return x
​
def gcd(lst):
  g = find_gcd(lst[0], lst[1])
  for i in range(2, len(lst)):
    g = find_gcd(g, lst[i])
  return g

