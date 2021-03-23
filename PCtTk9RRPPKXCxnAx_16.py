"""


The **modulo operation** can also be done by **repetitive subtraction or
addition**. In this challenge, you're going to create a function that mimics
such an operation and returns the modulo of the two given numbers by
**recursively** subtracting or adding them.

### Examples

    modulo(100, 25) ➞ 0
    
    modulo(-51, -4) ➞ -3
    
    modulo(3, 9) ➞ 3
    
    modulo(-21, 5) ➞ -1
    # -1 instead of 4 (which is what actually Python 
    # yields with the modulo operator %)
    
    modulo(1024, 7) ➞ 2
    
    modulo(273, -6) ➞ 3

### Notes

  * There will be no **zero-values** for the _modulo divisor_.
  * You're expected to solve this challenge using a **recursive approach**.
  * You can read on more topics about recursion (see **Resources** tab) if you aren't familiar with it yet or haven't fully assumed the concept behind it before taking up this challenge.

"""

def modulo(x, y):
  if x - y == 0:
    return 0
  elif abs(x) < abs(y):
    return x
  is_x_negative = x < 0
  is_y_negative = y < 0
  if ((is_x_negative and not is_y_negative)
    or (not is_x_negative and is_y_negative)
  ):
    return modulo(x + y, y)
  return modulo(x - y, y)

