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
    pool = list(range(1,n+1))
    kr_idx = 0
    while len(pool)>1:
        kd_idx = (kr_idx+1)%len(pool)
        kr_idx = (kr_idx+1)%len(pool)%(len(pool)-1)
        pool = pool[:kd_idx] + pool[kd_idx+1:]
    return pool[0]

