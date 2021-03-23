"""
A **Harshad** number is a number which is divisible by the sum of its digits.
For example, 132 is divisible by 6 (1+3+2).

A subset of the Harshad numbers are the **Moran** numbers. Moran numbers yield
a prime when divided by the sum of their digits. For example, 133 divided by 7
(1+3+3) yields 19, a prime.

Create a function that takes a number and returns `"M"` if the number is a
Moran number, `"H"` if it is a (non-Moran) Harshad number, or `"Neither"`.

### Examples

    moran(132) ➞ "H"
    
    moran(133) ➞ "M"
    
    moran(134) ➞ "Neither"

### Notes

N/A

"""

def moran(n):
  def fact(f):
   return [i for i in range(1,f+1) if f%i == 0]
  l = sum([int(i) for i in list(str(n))])
  if n%l == 0 and len(fact(n//l))== 2:
   return "M"
  if n%l == 0 and len(fact(n//l)) != 2:
   return "H"
  else:
   return "Neither"

