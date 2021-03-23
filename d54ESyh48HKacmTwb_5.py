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
  d = lst[0]
  for n in lst[1:]:
    d = gcd2(d,n)
  return d
​
def gcd2(a,b):
  while a:
    a,b = b%a,a
  return b

