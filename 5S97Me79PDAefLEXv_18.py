"""


Given a piece of code with a function assigned by **lambda** , rewrite it into
a function assigned by **def**. The code given would be in **string**.

### Overview

This is a quick example of a **lambda** expression:

    func = lambda a, b: a * (b - 2)

... is the same as ...

    def func(a, b):
      return a * (b - 2)

### Examples

    lambda_to_def("func = lambda w: w + 'lambda'") ➞ "def func(w):\n\treturn w + 'lambda'"
    
    lambda_to_def("z = lambda lambdadef: lambdadef.split(':')") ➞ "def z(lambdadef):\n\treturn lambdadef.split(':')"

Visualisation:

    print(lambda_to_def("func = lambda w: w + 'lambda'"))
    
    def func(w):
      return w + 'lambda'
    print(lambda_to_def("z = lambda lambdadef: lambdadef.split(':')"))
    
    def z(lambdadef):
      return lambdadef.split(':')

### Notes

  * The new code should follow PEP8 guidelines.
  * For the sake of convenience, use `\t` for indentation.
  * Assume all lambda expressions are valid.

"""

def lambda_to_def(code):
  import re
  from collections import Counter
  after_lambda = code.split("lambda ",1)[1]
  for i, j in enumerate(after_lambda):
    if j == ":" and Counter(after_lambda[:i])["'"]%2 == 0:
      arg_list = after_lambda[:i]
      return_value = after_lambda[i+1:]
  return "def " + code.split(" =")[0] + "(" + arg_list + "):\n\treturn" \
  + return_value

