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

def lambda_to_def(code: str) -> str:
  name = code[:code.find('=')].rstrip()
  code = code[code.find('lambda') + 6:].lstrip()
  quotes = []
  for i in range(len(code)):
    if code[i] == ':' and len(quotes) == 0:
      break
    elif code[i] in ("'", '"'):
      if len(quotes) > 0 and code[i] == quotes[-1]:
        quotes.pop()
      else:
        quotes.append(code[i])
  args, func = code[:i].rstrip(), code[i + 1:].strip()
  return 'def {}({}):\n\treturn {}'.format(name, args, func)

