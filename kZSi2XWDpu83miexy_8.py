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
  final = ''
  stack = []
  for i in expr.split():
    if i.isdigit():
      stack.append(i)
    else:
      res = str(stack[0]+i+stack[1])
      stack = [res]+stack[2:]
      final+=res
  return eval(res)

