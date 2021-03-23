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

def gcd2(a, b):
    while b != 0:
       t = b
       b = a % b
       a = t
    return a
​
def gcd(lst):
  g = gcd2(lst[0], lst[1])
  for k in lst[2:]:
    g = gcd2(g, k)
  return g

