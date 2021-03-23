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

def finished(x):
    count = 0
    for i in range(len(x)):
        if x[i] == 1:
            count += 1
    if count == 1:
        return True
    else:
        return False
​
def find_next(x, a):
    found = False
    index = a + 1
    while found == False:
        if x[index % len(x)] == 1:
            found = True
            return index % len(x)
        else:
            index += 1
​
def josephus(n):
    x = [1 for i in range(n)]
    while finished(x) == False:
        for i in range(len(x)):
            if x[i] == 1:
                x[find_next(x,i)] = 0
    return find_next(x,0) + 1

