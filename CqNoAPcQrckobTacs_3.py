"""


Create a function that takes a list of increasing letters and return the
missing letter.

### Examples

    missing_letter(["a", "b", "c", "e", "f", "g"]) ➞ "d"
    
    missing_letter(["O", "Q", "R", "S"]) ➞ "P"
    
    missing_letter(["t", "u", "v", "w", "x", "z"]) ➞ "y"
    
    missing_letter(["m", "o"]) ➞ "n"

### Notes

  * Tests will always have exactly one letter missing.
  * The length of the test list will always be at least two.
  * Tests will be in one particular case (upper or lower but never both).

"""

def missing_letter(lst):
  
  a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z' + ' a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper()
  a = a.split()
  
  indexes = []
  
  for l8r in lst:
    for n in range(0, len(a)):
      tl8r = a[n]
      if tl8r == l8r:
        indexes.append(n)
  
  indexes = sorted(indexes)
  
  wanted = []
  
  for n in range(indexes[0], indexes[-1] + 1):
    wanted.append(a[n])
  
  for item in wanted:
    if item not in lst:
      return item

