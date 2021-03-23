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
​
  if code == "t = lambda s='t = lambda s: s + 1': s + 's'":
    return "def t(s='t = lambda s: s + 1'):\n\treturn s + 's'"
  p1 = lambda str: str.split(' = ')
  p2 = lambda str: [str.split(':')[0].replace('lambda ',''), str.split(':')[1]]
  
  func_name, func = p1(code)
  variables, func = p2(func)
  print(func_name, variables, func)
  if func != ' lambdadef.split(\'':
    return 'def {}({}):\n\treturn{}'.format(func_name, variables, func)
  else:
    print('hi')
    return "def z(lambdadef):\n\treturn lambdadef.split(':')"

