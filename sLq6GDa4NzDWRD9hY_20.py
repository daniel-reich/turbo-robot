"""


Create a function that _counts_ the integer's **number of digits**.

### Examples

    count(318) ➞ 3
    
    count(-92563) ➞ 5
    
    count(4666) ➞ 4
    
    count(-314890) ➞ 6
    
    count(654321) ➞ 6
    
    count(638476) ➞ 6

### Notes

  * Solve this **without using strings**.
  * Alternatively, you can solve this via a _recursive approach_.
  * A _recursive_ version of this challenge can be found via this [link](https://edabit.com/challenge/ntJXZh4W8khX9nLPG).

"""

import math
def count(n):
    if n>0:
        digits = int(math.log10(n))+1
    elif n == 0:
        digits = 1
    else: 
        digits = int(math.log10(-n))+1
    return digits

