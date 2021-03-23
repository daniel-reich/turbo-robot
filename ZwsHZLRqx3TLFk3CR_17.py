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

from math import factorial as fact
​
def eval_factorial(lst):
  nums = map(lambda s: int(s[:-1]),
             lst)
  return sum(map(fact, nums))

