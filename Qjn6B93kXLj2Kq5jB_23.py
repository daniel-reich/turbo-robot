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
  lst = [int(i) for i in f.split("/")]
  a=lst[0]
  b=lst[1]
  alst=[a]
  blst=[]
  for x in range(1,a):
    if a % x == 0:
      alst.append(x)
  for y in range(1,b):
    if b % y == 0:
      blst.append(y)
  reslst=[i for i in blst if i in alst]
  answer=[str(int(i/reslst[-1])) for i in lst]
  return "/".join(answer)

