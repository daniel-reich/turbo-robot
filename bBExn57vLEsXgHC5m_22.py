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

def same_line(ls: list) -> bool:
    if ls[0][0] == ls[1][0]:
        if ls[0][0] == ls[2][0]:
            return True
        else:
            return False
    a = (ls[0][1] - ls[1][1]) / (ls[0][0] - ls[1][0])
    b = ls[0][1] - a * ls[0][0]
    return ls[2][1] == a * ls[2][0] + b

