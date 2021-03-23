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

def josephus(n):
    if n == 1: return n
    pri = [i for i in range(n)]
    sur = [i for i in pri if i not in pri[1::2]]
    pri = ['-']*len(pri) + sur
    while len(sur) > 1:
        sur = [i for i in pri if i not in pri[1::2]]
        pri = ['-']*len(pri) + sur
    return sur[0]+1

