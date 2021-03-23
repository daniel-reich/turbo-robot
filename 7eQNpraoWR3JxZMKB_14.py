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
  if a > b:
    mx = a
    mn = b
  elif a < b:
    mx = b
    mn = a
  elif a == b:
    return 0
  mn = (~mn) + 1
  return mx + mn

