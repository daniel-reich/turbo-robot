"""


Create a function that takes a function `func` and counts its arguments.
Examining a function's bytecode using `__code__` is disabled.

### Examples

    num_args(lambda: "") ➞ 0
    
    num_args(lambda x: "") ➞ 1
    
    num_args(lambda x, y: "") ➞ 2

### Notes

  * All random test function expressions will be constructed using `+`, `-`, `*`, and `/`.
  * None of the parameters of `func` will have default values.
  * All functions will be converted to a custom class object to avoid use of `__code__`.
  * If disabling `__code__` or removing function functionality is too harsh, feel free to leave a comment.

"""

def num_args(func, n=0):
  try: eval('func(%s)' % ('1,'*n)); return n
  except: return num_args(func, n+1)

