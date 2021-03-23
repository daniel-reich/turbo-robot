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
  lst = sorted(lst)
  g = func(lst[0],lst[1])
  for i in range(2,len(lst)):
    g = func(g,lst[i])
  return g
  
def func(a,b):
  if b%a==0:
    return a
  return func(b,a%b)

