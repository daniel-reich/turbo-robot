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
  pieces = expr.split()
  nums = [p for p in pieces if p.isnumeric()]
  ops = [p for p in pieces if not p.isnumeric()]
  
  curr = nums[0]
  
  for num,op in zip(nums[1:],ops):
    curr = str(int(eval(curr+op+num)))
  
  return int(curr)

