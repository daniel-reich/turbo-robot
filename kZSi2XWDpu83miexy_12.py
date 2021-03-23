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

def post_fix(ops):
  ops = ops.split()
​
  while len(ops) > 1:
    i = 0
    while ops[i] not in '+-*/':
      i += 1
​
    op = ops.pop(i)
    n1 = ops.pop(0)
    n2 = ops.pop(0)
​
​
    ops.insert(0, str(eval(n1 + op + n2)))
​
  return eval(ops[0])

