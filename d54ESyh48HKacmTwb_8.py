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

def gcd_n(a, b):
  return a if b==0 else gcd_n(b, a%b)
def gcd(lst):
  return gcd_n(lst[0], lst[1]) if len(lst)==2 else gcd_n(lst[0], gcd(lst[1:]))

