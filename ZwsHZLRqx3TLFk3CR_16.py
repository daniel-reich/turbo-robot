"""


Create a function that takes a list of factorial expressions and returns the
sum.

### Examples

    eval_factorial(["2!", "3!"]) ➞ 8
    
    eval_factorial(["5!", "4!", "2!"]) ➞ 146
    
    eval_factorial(["0!", "1!"]) ➞ 2

### Notes

0! and 1! both equal 1.

"""

def fac(n):
  if n==0 or n==1:
    return 1
  return n*fac(n-1) 
def eval_factorial(lst):
  return sum([fac(int(l[:-1])) for l in lst])

