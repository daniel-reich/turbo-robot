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
    y=[]
    eq=eq.replace('=','==')
    for i in range(-10,10):
        x=i
        if eval(eq):
            y.append(float(i))
    if len(y)==0:
        return "Infinite solutions"
    return y[0]

