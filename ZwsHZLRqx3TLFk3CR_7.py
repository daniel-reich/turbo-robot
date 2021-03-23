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

def f(x):
  r=1
  for i in range(2,int(x[:-1])+1):
    r*=i
  return r
​
def eval_factorial(lst):
  return sum(map(f,lst))

