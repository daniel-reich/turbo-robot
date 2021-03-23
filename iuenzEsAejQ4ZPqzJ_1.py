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

def mystery_func(num):
  int_root = int(num**0.5)
  return int('2' * int_root + str(num - 2**int_root))

