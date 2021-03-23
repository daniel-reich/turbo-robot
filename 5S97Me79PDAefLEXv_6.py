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
    code=code.split(" ")
    for index, i in enumerate(code):
        if i[-1]==":" :
            g=index
    if int(g)==3:
        gen = code[g]
        kew=int(len(gen)-1)
        gen= gen[:kew]
        vr ="def"+" "+ code[0] + "(" + gen + ")"
    else:
        cod=code[3:int(g)]
        cod=" ".join(cod)
        gen = code[g]
        kew = int(len(gen) - 1)
        gen = gen[:kew]
        vr="def"+" "+code[0]+"("+cod+" "+gen+")"
    f = code[int(g) + 1:]
    f = " ".join(f)
    f=":\n\treturn"+" "+f
    final=vr+f
    return(final)

