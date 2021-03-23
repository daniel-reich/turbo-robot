"""


Write a function that swaps the X and Y coordinates in a string.

### Examples

    swap_xy("(1, 2), (3, 4)") ➞ "(2, 1), (4, 3)"
    
    swap_xy("(11, 23), (43, 99)") ➞ "(23, 11), (99, 43)"
    
    swap_xy("(-5, -3), (7, 4)") ➞ "(-3, -5), (4, 7)"

### Notes

  * Some numbers have multiple digits.
  * Some numbers will be negative.

"""

import re
def swap_xy(txt):
    result = [int(i) for i in re.findall(r'-?\d+', txt)]
    print(result)
    for i in range(len(result)):
        if i%2 == 0:
            result[i], result[i+1] = result[i+1], result[i]
    return "("+str(result[0])+", "+str(result[1])+"), ("+str(result[2])+", "+str(result[3])+")"

