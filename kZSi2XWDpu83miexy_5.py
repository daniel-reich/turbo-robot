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

import re
def post_fix(expr):
  A=re.findall('\d\d?', expr)
  B=re.findall('[\+\-\*\/]', expr)
  C=[j for i in zip(A,B) for j in i]+[A[-1]]
  return eval(''.join(C))

