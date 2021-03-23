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
  f_lst = f.split("/")
  numerator, denominator = int(f_lst[0]), int(f_lst[1])
  numer, denom = int(f_lst[0]), int(f_lst[1])
  while denom:
    numer, denom = denom, numer % denom
  return str((numerator // numer)) + "/" + str((denominator // numer))

