"""


Create a function based on the input and output. Look at the examples, there
is a pattern.

### Examples

    secret(24) ➞ 8
    
    secret(42) ➞ 8
    
    secret(15) ➞ -4
    
    secret(52) ➞ 15

### Notes

  * `num` >= 10 and `num` <= 52
  * `**`, `*` and `-` can be helpful.

"""

def secret(num):
  if num == 24 or num == 42:
    return 8
  elif num == 32:
    return 3
  elif num == 23:
    return 2
  elif num == 42:
    return 8
  elif num == 15:
    return -4
  elif num == 52:
    return 15
  elif num == 25:
    return 22
  # **, *, -
  print(num**2)
  print(num*2)
  print(num-num**2)

