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
    p = {i: True for i in range(people)}
    alive = people
    cur = 0
    while alive > 1:
        cur = (cur + 1) % people
        while not p[cur]:
            cur = (cur + 1) % people
        p[cur] = False
        alive -= 1
        while not p[cur]:
            cur = (cur + 1) % people
    return [k+1 for k, v in p.items() if v][0]

