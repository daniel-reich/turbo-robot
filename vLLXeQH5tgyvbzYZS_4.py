"""


A Pythagorean triple is a set of three integer numbers that form a right
triangle. The sum of the squares of the two smaller numbers should equal the
square of the largest number. Given three numbers a, b and c (c being the
largest):

    a^2 + b^2 = c^2

Furthermore, a Pythagorean triple is said to be primitive if the three numbers
are pairwise coprime - that is, the greatest common prime factor between any
two numbers is 1.

Create a function that takes a list of three numbers (unordered) and returns
`True` if the numbers constitute a primitive Pythagorean triple, `False`
otherwise.

### Examples

    is_prim_pyth_triple([4, 5, 3]) ➞ True
    
    is_prim_pyth_triple([7, 12, 13]) ➞ False
    
    is_prim_pyth_triple([39, 15, 36]) ➞ False
    # Pythagorean triple, but not primitive.
    
    is_prim_pyth_triple([77, 36, 85]) ➞ True

### Notes

N/A

"""

def is_prim_pyth_triple(lst):
  a, b, c = sorted(lst)
  if a**2 + b**2 == c**2:
    a_f = get_prime_factors(a)
    b_f = get_prime_factors(b)
    c_f = get_prime_factors(c)
    
    if not a_f & b_f & c_f:
      return True
  return False
​
def get_prime_factors(n):
  facts = set()
  for i in range(2,n):
    while not n%i:
      if i not in facts:
        facts.add(i)
      n //= i
  return facts

