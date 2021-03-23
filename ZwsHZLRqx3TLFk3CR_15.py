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
  def fact(f):
   if f == 0:
    return 1
   else :
    return f*fact(f-1)
  lst1 = [int(x.strip("!")) for x in lst]
  return sum([fact(x) for x in lst1])

