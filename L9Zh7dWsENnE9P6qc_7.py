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
    prisoners = []
    for x in range(people):
        prisoners.append(str(x+1))
    count = 1
    while len(prisoners)>1:
        if count>=len(prisoners):
            count -= len(prisoners)
            continue
        prisoners.pop(count)
        count += 1
    return int(prisoners[0])

