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
    lst = eq.split()
    if lst.index("x") == 4:
        if lst[1] == "+":
            return int(lst[0]) + int(lst[2])
        else:
            return int(lst[0]) - int(lst[2])
    if lst.index("x") == 2:
        if lst[1] == "+":
            return int(lst[4]) - int(lst[0])
        else:
            return int(lst[0]) - int(lst[4])
​
    if lst.index('x') == 0:
        if lst[1] == '+':
            return int(lst[4]) - int(lst[2])
        else:
            return int(lst[4]) + int(lst[2])

