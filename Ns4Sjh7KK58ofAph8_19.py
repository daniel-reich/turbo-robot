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
      ln=list([n1,n2,n3])
      ln.sort()
      if ln[0]*ln[0]+ln[1]*ln[1]==ln[2]*ln[2]:
            return True
      return False

