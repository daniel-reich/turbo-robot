"""


Given a _string_ containing an _algebraic equation_ , calculate and **return
the value of x**. You'll only be given equations for simple **addition** and
**subtraction**.

### Examples

    eval_algebra("2 + x = 19") ➞ 17
    
    eval_algebra("4 - x = 1") ➞ 3
    
    eval_algebra("23 + 1 = x") ➞ 24

### Notes

  * There are spaces between every number and symbol in the string.
  * x may be a negative number.

"""

def eval_algebra(eq):
    li = eq.split(' ')
    eq_pos, var_pos = li.index('='), li.index('x')
    if var_pos == 0 and eq_pos == 1:
        return eval(''.join(li[2:]))
    n = len(eq)
    if li[-1] == 'x' and li[-2] == '=':
        return eval(''.join(li[:eq_pos]))
    if var_pos > eq_pos:
        li = li[eq_pos + 1:] + ['='] + li[:eq_pos]
        eq_pos, var_pos = li.index('='), li.index('x')
    oper = li[1]
    if var_pos == 0:
        if oper == "+":
            return int(li[-1]) - int(li[2])
        else:
            return int(li[-1]) + int(li[2])
    else:
        if oper == "+":
            return int(li[-1]) - int(li[0])
        else:
            return -1*(int(li[-1]) - int(li[0]))

