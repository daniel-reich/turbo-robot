"""


In this challenge, you have to permutate an expression that includes three
variable values `a`, `b` and `c`. You are given a set of three unique numbers
to substitute for letters so there are six possible different expression
variations, and you have to find which one returns the greater result.

    expr = "(a - b) * c" | nums = [1, 2, 3]
    
    Permutation #1 ➞ (1 - 2) * 3 = -3
    Permutation #2 ➞ (1 - 3) * 2 = -4
    Permutation #3 ➞ (2 - 1) * 3 = 3
    Permutation #4 ➞ (2 - 3) * 1 = -1
    Permutation #5 ➞ (3 - 1) * 2 = 4
    Permutation #6 ➞ (3 - 2) * 1 = 1
    
    # Permutation #5 returns the greater result.

Given an expression string `expr` and a list of three numbers `nums`, the
function must return a string with the complete notation of the expression
that returns the greater result (adding the equal sign after the expression
and the result after the equal sign). For the example above, the result will
be:

    greater_permutation("(a - b) * c", [1, 2, 3]) ➞ "(3 - 1) * 2 = 4"

If an expression returns a float number as result, round it to the nearest
hundredth.

### Examples

    greater_permutation("(a - b) * c", [1, 2, 3]) ➞ "(3 - 1) * 2 = 4"
    
    greater_permutation("a ** b - c", [2, 3, 1]) ➞ "3 ** 2 - 1 = 8"
    
    greater_permutation("a % b + (c * 2)", [3, 1, 2]) ➞ "1 % 2 + (3 * 2) = 7"

### Notes

  * Every given expression is designed to have just one permutation that returns a maximum result, don't worry about multiple matches.
  * Expressions can contain known values besides the three variables (see example #3).
  * Remember to round to the nearest hundredth if the result is a float number.

"""

from itertools import permutations
import re
def greater_permutation(expr, nums):
  def express(perm):
    expression = expr
    for a,b in zip(perm,['a','b','c']):
      expression = expression.replace(b,str(a))
    return expression
  def result(perm):
    string = express(perm)
    while True:
      if not "(" in string:
        return eval(string)
      string = re.sub(r'(\()([^\(\)]+)(\))',lambda x: str(eval(x.group(2))),string)
  perms = sorted(list(permutations(nums)),key = lambda x: result(x))
  n = result(perms[-1])
  if isinstance(n,int):
    s = str(n)
  elif bool(re.search(r'\.0$',str(n))) == True:
    s = re.sub(r'\.0$','',str(n))
  else:
    s = str(round(n,2))
  return "{} = {}".format(express(perms[-1]),s)

