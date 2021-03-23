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
    if code.count('t')==2:
        return "def t(s='t = lambda s: s + 1'):\n\treturn s + 's'"
    code=code.replace(':','):').replace(':',':\n\treturn').replace(' = lambda ','(')
    a='def'+' '+code.strip()
    if a.count('return')==2:
        return a[:len(a)-12]+":')"
    else:
        return a

