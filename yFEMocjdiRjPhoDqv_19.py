"""


Create a function that returns `True` if there's at least one prime number in
the given range (`n1` to `n2` (inclusive)), `False` otherwise.

### Examples

    prime_in_range(10, 15) ➞ True
    # Prime numbers in range: 11, 13
    
    prime_in_range(62, 66) ➞ False
    # No prime numbers in range.
    
    prime_in_range(3, 5) ➞ True
    # Prime numbers in range: 3, 5

### Notes

  * `n2` is always greater than `n1`.
  * `n1` and `n2` are always positive.
  * 0 and 1 aren't prime numbers.

"""

def f(m):
  s=0
  if m<2: return False
  else:
    for i in range(1,m+1):
      if m%i==0: s+=1
    return s==2
def prime_in_range(n1, n2):
  return any(map(f,range(n1,n2+1)))

