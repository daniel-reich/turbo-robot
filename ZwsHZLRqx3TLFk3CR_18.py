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
  def fact(n):
    return 1 if n<=1 else n*fact(n-1)
  return sum(fact(int(n[:-1])) for n in lst)

