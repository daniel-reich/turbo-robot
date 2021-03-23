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

def solver(equ):
    '''
    Returns the solution to the 1st degree equation equ if there is one, or
    'Infinite solutions' otherwise.
    '''
    x_mult = 0  # multiplier for the x
    total = 0 # tracks the total numeric value
    operators = ('-', '+')
    terms = equ.split()
    equ_loc = terms.index('=')
    
    x_mag = lambda x: 1 if len(x) == 1 else int(x[0:x.index('*')])
    num_val = lambda x: eval(x)
    is_x = lambda x: x.count('x') == 1
    is_num = lambda x: x.count('x') == 0
​
    i = 0
    while i < equ_loc:  # LHS of equation
        term = terms[i]
        if term in operators:
            if is_x(terms[i+1]): # x term next
                x_mult = eval('x_mult {} x_mag(terms[i+1])'.format(term))
            elif is_num(terms[i+1]):
                op = operators[not operators.index(term)] # reverse operator
                total = eval('total {} num_val(terms[i+1])'.format(op))
            i += 1  # skip next term too
        elif is_x(term):
            x_mult += x_mag(term)
        elif is_num(term):
            total -= eval(term)  # reversed when on rhs of equation
        i += 1
​
    # Assume just 1 term on RHS: number or multiple of x
    i += 1
    term = terms[i]
    if is_x(term):
        x_mult -= x_mag(term)  # move to LHS
    else:
        total += eval(term)
​
    return 'Infinite solutions' if x_mult == 0 else total / x_mult

