"""


In chess, queens can move any number of squares horizontally, vertically or
diagonally.

Given the location of your queen and your opponents' queen, determine whether
or not you're able to capture your opponent's queen. Your location and your
opponents' location are the first and second elements of the list,
respectively.

### Examples

    can_capture(["A1", "H8"]) ➞ True
    # Your queen can move diagonally to capture opponents' piece.
    
    can_capture(["A1", "C2"]) ➞ False
    # Your queen cannot reach C2 from A1 (although a knight could).
    
    can_capture(["G3", "E5"]) ➞ True

### Notes

Assume there are no blocking pieces.

"""

import numpy as np
def can_capture(x):
    lst = np.array([chr(i)+str(j) for i in range(65,73) for j in range(1,9)])
    lst2 = lst.reshape((8,8))
    (a,b) = np.where(lst2==x[0])[0][0]+1,np.where(lst2==x[0])[1][0]+1
    (c,d) = np.where(lst2==x[1])[0][0]+1,np.where(lst2==x[1])[1][0]+1
    if ((a==c) or (b==d)) or abs(a-c)==abs(b-d):
        return True
    else:
        return False

