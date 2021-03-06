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

def post_fix(expr):
    expr = expr.split(' ')
    num = []
    for i in expr:
        if i.isdigit():
            num.append(i)
        else:
            num = [int(eval(str(num[0]) + i + num[1]))] + num[2:]        
    return num[0]

