"""
Given a list of four points in the plane, determine if they are the vertices
of a parallelogram.

### Examples

    is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)]) ➞ True
    
    is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)]) ➞ False
    
    is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]) ➞ True

### Notes

The points may be given in any order (compare examples #1 and #5).

"""

def is_parallelogram(lst):
    gradients = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j][0] - lst[i][0] == 0 and lst[j][1] - lst[i][1] == 0:
                print("Duplicated points!")
                return False
            elif lst[j][0] - lst[i][0] == 0 and lst[j][1] - lst[i][1] != 0:
                grad = 1e20
            else:
                grad =  (lst[j][1] - lst[i][1]) / (lst[j][0] - lst[i][0])
            gradients.append(grad)
    dup_grads = []
    for i in range(len(gradients)):
        dup = 0
        for j in range(len(gradients)):
            if gradients[i] == gradients[j]:
                dup += 1
        dup_grads.append(dup)
    dup_2 = 0
    for i in range(len(dup_grads)):
        if dup_grads[i] == 2:
            dup_2 += 1
        if dup_grads[i] >= 3:
            print("4 points do not constitute a quadrangle!!!")
            return False
    if dup_2 == 4:
        return True
    else:
        return False

