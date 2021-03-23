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
  nums = [i for i in expr.split() if i.isdigit()]
  ops = [i for i in expr if i in '+-*/'] + [' ']
  result = ''
  for i in range(len(nums)):
    result += nums[i] + ops[i]
  return int(eval(result))

