"""


Create a function that takes a mathematical expression in **prefix notation**
as a string and evaluates the expression.

### Examples

    prefix("+ 5 4") ➞  9
    
    prefix("* 12 2") ➞  24
    
    prefix("+ -10 10") ➞  0

### Notes

  * The mathematical expression is valid.
  * Check the **Resources**.
  * Use `//` for division.

"""

def prefix(exp):
    ops, nums = [], []
    lst_exp = exp.split()
    while lst_exp:
        if lst_exp[0] in '+-*/' and lst_exp[1][-1].isnumeric():
            nums.append(str(int(eval(lst_exp[1] + lst_exp[0] + lst_exp[2]))))
            lst_exp = lst_exp[3:]
            continue
        elif lst_exp[0] in '+-*/':
            ops.append(lst_exp[0])
        elif lst_exp[0][-1].isnumeric() and nums:
            nums.append(str(int(eval(nums.pop() + ops.pop() + lst_exp[0]))))
        elif lst_exp[0][-1].isnumeric():
            nums.append(lst_exp[0])
        lst_exp = lst_exp[1:]
    if len(nums) > 1:
        a, b = nums.pop(), nums.pop()
        return int(eval(b + ops.pop() + a))
    return int(nums.pop())

