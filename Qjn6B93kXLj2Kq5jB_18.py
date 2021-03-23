"""


Create a function which _simplifies_ a given **fraction** into its **simplest
ratio**. Return the fraction as a _string_.

### Examples

    simplify_frac("2/4") ➞ "1/2"
    
    simplify_frac("15/25") ➞ "3/5"
    
    simplify_frac("4/9") ➞ "4/9"

### Notes

  * Fractions are given as strings.
  * Return the same fraction if it is already in its simplified ratio (see example #3).

"""

def simplify_frac(f):
  parts = f.split('/')
  numerator = int(parts[0])
  denominator = int(parts[1])
  reduce = 1
  for i in range(2,denominator+1):
    if denominator % i == 0 and numerator % i == 0:
      if i > reduce:
        reduce = i
  return str(int(numerator / reduce))+'/'+str(int(denominator/reduce))

