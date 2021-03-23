"""


Create a function that returns `True` if three points belong to the same line,
and `False` otherwise. Each point is represented by a list consisting of an x-
and y-coordinate.

### Examples

    same_line([[0, 0], [1, 1], [3, 3]]) ➞ True
    
    same_line([[-2, -1], [2, 1], [0, 0]]) ➞ True
    
    same_line([[-2, 0], [-10, 0], [-8, 0]]) ➞ True
    
    same_line([[0, 0], [1, 1], [1, 2]]) ➞ False
    
    same_line([[3, 4], [3, 5], [6, 6]]) ➞ False

### Notes

Note the special case of a vertical line.

"""

def same_line(lst):
    try:
        m = (lst[1][1]-lst[0][1])/(lst[1][0]-lst[0][0])
    except:
            if lst[0][0] == lst[1][0] == lst[2][0]:
                return True
            else:
                return False
    c = lst[0][1]-m*lst[0][0]
    y = lst[2][1]
    x = lst[2][0]
    return y == m*x+c

