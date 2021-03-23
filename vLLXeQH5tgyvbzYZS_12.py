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
  """ 
  Return if a^2 + b^2 = c^2 is true
  AND
  the greatest common prime factor between any two numbers is 1.
​
  >>> is_prim_pyth_triple([4, 5, 3])
  True
  >>> is_prim_pyth_triple([7, 12, 13])
  False
  >>> is_prim_pyth_triple([39, 15, 36])
  False
  >>> is_prim_pyth_triple([77, 36, 85])
  True
​
  """
  l = sorted(lst)
  a, b, c = l[0], l[1], l[2]
​
  # Find GCP of all three numbers
  a_factors = [i for i in range(1, a + 1) if a % i == 0]
  b_factors = [i for i in range(1, b + 1) if b % i == 0]
  c_factors = [i for i in range(1, c + 1) if c % i == 0]
​
​
  common = [i for i in range(1, c + 1) if (i in a_factors) and (i in b_factors) and (i in c_factors)]
​
  return (a**2 + b**2 == c**2) and (common == [1])

