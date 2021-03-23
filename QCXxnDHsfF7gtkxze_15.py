"""


This is a **reverse coding challenge**. Normally you're given explicit
directions with how to create a function. Here, you must generate your own
function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produces
the sample outputs shown.

### Examples

    mystery_func(152) ➞ 10
    
    mystery_func(832) ➞ 48
    
    mystery_func(19) ➞ 9
    
    mystery_func(133) ➞ 9

### Notes

N/A

"""

def mystery_func(num):
  r = 1
  while num:
    r *= (num % 10)
    num //= 10
  return r

