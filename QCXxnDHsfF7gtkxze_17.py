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

import numpy as np
def mystery_func(num):
  min_num = int(str(num)[0])
  max_num = int(str(num)[-1])
  
  return min_num * max_num * np.prod([int(x) for x in str(num)][1:-1])

