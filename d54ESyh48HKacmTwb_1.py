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

from functools import reduce
def calc(a,b):
  while b:
    a,b = b,a%b
  return a
def gcd(lst):
  return reduce(lambda x,y: calc(x,y),lst)

