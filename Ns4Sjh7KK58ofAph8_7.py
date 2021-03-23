"""


Create a function that validates whether three given integers form a
**Pythagorean triplet**. The sum of the squares of the _two smallest integers_
must equal the square of the _largest number_ to be validated.

### Examples

    is_triplet(3, 4, 5) ➞ True
    # 3² + 4² = 25
    # 5² = 25
    
    is_triplet(13, 5, 12) ➞ True
    # 5² + 12² = 169
    # 13² = 169
    
    is_triplet(1, 2, 3) ➞ False
    # 1² + 2² = 5
    # 3² = 9

### Notes

Numbers may not be given in a sorted order.

"""

def is_triplet(n1, n2, n3):
  n = max(n1,n2,n3)
  sum = n1*n1 + n2*n2 + n3*n3 - n*n
  return sum==n*n

