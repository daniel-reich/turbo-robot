"""


Create a function that takes a string and returns the right answer.

### Examples

    post_fix("2 2 +") ➞ 4
    
    post_fix("2 2 /") ➞ 1
    
    post_fix("8 4 / 9 * 3 1 * /") ➞ 54

### Notes

  * The operators `+ - * /` may be supported.
  * Output always returns an integer.

"""

OPER = {'+':int.__add__,'-':int.__sub__,'*':int.__mul__,'/':int.__floordiv__}
​
def post_fix(expr):
    oper = (n for n in expr.split() if n in '+-*/')
    a, *nums = (int(n) for n in expr.split() if n not in '+-*/')
    for o, b in zip(oper, nums):
        a = OPER[o](a, b)
    return a

