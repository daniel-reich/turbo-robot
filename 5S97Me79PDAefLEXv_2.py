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

def lambda_to_def(c):
  f,b=c.strip().split(':',1)
  if'"'in f or"'"in f:
    c=c.strip().split(':')
    f,b=c[0]+':'+c[1],c[2]
  f,p=f.strip().split('=',1)
  f,p,b=f.strip(),p.strip(),b.strip()
  i=p.find(' ')
  p=p[i+1:]if i>=0else''   
  return"def %s(%s):\n\treturn %s"%(f,p,b)

