"""


This is a **reverse coding challenge**. Normally you're given explicit
directions with how to create a function. Here, you must generate your own
function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produce the
sample outputs shown.

### Examples

    3 ➞ 21
    
    9 ➞ 2221
    
    17 ➞ 22221
    
    24 ➞ 22228

### Notes

If you get stuck, check the **Comments** for help.

"""

from math import log
​
def mystery_func(num):
  n = int(log(num,2))
  l = num - 2**n
  return int(n*'2' + str(l))
