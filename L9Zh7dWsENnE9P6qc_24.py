"""


Given `n` people find the survivor, starting from the first person he kills
the person to the left and the next surviving person kills the person to his
left, this keeps happening until 1 person survives return that person's
number.

### Examples

    josephus(1) ➞ 1
    
    josephus(8) ➞ 1
    
    josephus(41) ➞ 19

### Notes

Check the rescources if you are confused about the instructions.

"""

import math
def josephus(people):
    x = people - 2 ** math.floor(math.log2(people))
    if math.log2(people) % 1 == 0:
        return 1
    return 2 * x + 1

