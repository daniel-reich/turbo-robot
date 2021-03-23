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
​
    x_coords = [point[0] for point in lst]
    y_coords = [point[1] for point in lst]
    
    try:
        y_deltas = (y_coords[2] - y_coords[0]) / (y_coords[1] - y_coords[0])
        x_deltas = (x_coords[2] - x_coords[0]) / (x_coords[1] - x_coords[0])
        return y_deltas == x_deltas
    
    except ZeroDivisionError:
        if len(set(x_coords)) == 1 or len(set(y_coords)) == 1:
            return True
        return False

