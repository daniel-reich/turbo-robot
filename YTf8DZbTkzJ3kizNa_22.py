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
​
  def is_prime(num):
    for i in range(2, num):
      if num%i == 0:
        return False
    return True
    
  s = sum([int(x) for x in list(str(n))])
  if n%s == 0:
    if is_prime(n//s):
      return "M"
    else:
      return "H"
  else: 
    return "Neither"

