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

import re
def solver(eq):
    left, right = eq.split(' =')
    lst_a_x = re.findall(r'\d+\*x(?= |$)', left)
    lst_c_x = re.findall(r'\d+\*x(?= |$)|(?<= )x(?= |$)', right)
    b = eval(left.replace('x', '0'))
    d = eval(right.replace('x', '0'))
    a = sum(int(i[:-2]) if len(i) > 1 else 1 for i in lst_a_x)
    c = sum(int(i[:-2]) if len(i) > 1 else 1 for i in lst_c_x)
    return 'Infinite solutions' if a - c == 0 else (d - b) / (a - c)

