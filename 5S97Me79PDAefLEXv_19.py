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

import re
lambda_format = re.compile(r'(.*?)\s+=\s+lambda\s+(.*?):(.*)')
​
def lambda_to_def(code):
  m = lambda_format.match(code)
  if not m:
    return None
  name, args, expr = m.group(1), m.group(2), m.group(3)
  
  colon_replaced = False
  def fix_quote(quote):
    nonlocal args, expr, colon_replaced
    if args.count(quote) % 2 != 0:
      if not colon_replaced:
        args += ':'
        colon_replaced = True
      rouge_quote = expr.find(quote)
      args += expr[:rouge_quote + 1]
      expr = expr[rouge_quote + 1:]
      
  fix_quote("'")
  fix_quote('"')
  if expr[0] == ':':
    expr = expr[1:]
  return "def {}({}):\n\treturn {}".format(name.strip(), args.strip(), expr.strip())

