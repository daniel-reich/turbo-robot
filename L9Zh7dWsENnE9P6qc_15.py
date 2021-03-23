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

def josephus(people):
    if people == 1:
        return 1
    if people%2 == 0:
        return 2 * josephus(people / 2) - 1
    if people%2 == 1:
        return 2 * josephus((people - 1) / 2) + 1

