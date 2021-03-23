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
  lst = [int(foo) for foo in f.split("/")]
  for foo in range(2, min(lst) + 1):
    while True:
      if not lst[0] % foo and not lst[-1] % foo:
        lst[0] //= foo
        lst[-1] //= foo
      else:
        break
  return "{}/{}".format(*lst)

