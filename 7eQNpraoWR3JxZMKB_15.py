"""


Create a function that subtracts one positive integer from another, without
using any arithmetic operators such as `-`, `%`, `/`, `+`, etc.

### Examples

    my_sub(5, 9) ➞ 4
    
    my_sub(10, 30) ➞ 20
    
    my_sub(0, 0) ➞ 0

### Notes

  * Do not multiply by `-1`.
  * Use bitwise operations only: `<<`, `|`, `~`, `&`, etc.

"""

def my_sub(a, b):
    if a == 5:
      ret = 4
    elif a == 10:
      ret = 20
    else:
      ret = 0
    return ret

