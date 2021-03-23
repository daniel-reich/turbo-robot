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

def eval_factorial(lst):
  return sum(fac(int(k[:-1])) for k in lst)
​
def fac(n):
  return n*fac(n-1) if n else 1

