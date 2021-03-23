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
    lst = list(range(1, people + 1))
    count = 0
    while lst.count(0) != people - 1:
        for x in range(len(lst)):
            if lst[x] != 0:
                count += 1
                if count == 2:
                    lst[x] = 0
                    count = 0
    for x in lst:
        if x != 0:
            return x

