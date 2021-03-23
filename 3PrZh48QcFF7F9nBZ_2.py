"""


Create a function that takes a first-degree equation as a string and solves
it. If there would be more than one solution, the function must return
`"Infinite solutions"`.

### Examples

    solver("2*x + 1 = x") ➞ -1.0
    
    solver("7*x + x - 4 = 0") ➞ 0.5
    
    solver("x = x") ➞ "Infinite solutions"

### Notes

The given variable is always "x".

"""

def solver(eq):
    eq = eq.replace(" -", " + -").replace(' x', '1*x')
    side1, side2 = eq.split('=')
    coeff1 = [sum(eval(t.replace('*x', '')) for t in side1.split('+') if '*x' in t and '*x*' not in t),
              sum(eval(t.replace('*x', '')) for t in side1.split('+') if '*x' not in t)]
    coeff2 = [sum(eval(t.replace('*x', '')) for t in side2.split('+') if '*x' in t and '*x*' not in t),
              sum(eval(t.replace('*x', '')) for t in side2.split('+') if '*x' not in t)]
    return (coeff2[1]-coeff1[1])/(coeff1[0]-coeff2[0]) if coeff1[0]!=coeff2[0] else 'Infinite solutions'

