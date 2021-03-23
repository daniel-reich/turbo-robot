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
  b=[]
  for i in range(1,min(lst)+1):
    for a in lst:
      if a%i==0:
        b.append(i)
  c=[]
  for j in b:
    if b.count(j)==len(lst):
      c.append(j)
  return max(c)

