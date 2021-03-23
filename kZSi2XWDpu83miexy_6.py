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
  expr = expr.split()
  d,f = [i for i in expr if i.isdigit()],[i for i in expr if not i.isdigit()]
  for i in range(1,len(d)):
    d[i] = str(eval(d[i-1]+f[0]+d[i]))
    f = f[1:]
  return float(d[-1])

