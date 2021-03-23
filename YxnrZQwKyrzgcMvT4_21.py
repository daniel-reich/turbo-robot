"""


Create a function to rotate a two-dimensional matrix of `N * N` integer
elements `num` times, where if `num` is positive, the rotation is
**clockwise** , and if not, **counterclockwise**.

### Examples

    rotate_transform([
      [2, 4],
      [0, 0]
    ], 1) ➞ [
      [0, 2],
      [0, 4]
    ]
    rotate_transform([
      [2, 4],
      [0, 0]
    ], -1) ➞ [
      [4, 0],
      [2, 0]
    ]

### Notes

N/A

"""

def rotate_transform(lst, num):
    total_rotations = -num%4 # got the direction wrong
    temp = lst
    for _ in range(total_rotations):
        temp = rotate_once(temp)
    return temp
​
def rotate_once(lst):
    dimension = len(lst)
    temp = []
    for i in range(dimension):
      temp_row = []
      for j in range(dimension):
        temp_row.append(lst[j][dimension-1-i])
      print(temp_row)
      temp.append(temp_row)
    return temp
​
a= [[1,2,3],[4,5,6],[7,8,9]]
rotate_once(a)

