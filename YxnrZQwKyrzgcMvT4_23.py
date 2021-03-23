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

lst = [
    [1, 4, 0, 0],
    [2, 8, 0, 0],
    [0, 0, 3, 5],
    [0, 0, 7, 1]
      ]
num = -1
def rotate_transform(lst,num):
    def clockwise(lst):
        c = []
        for i in range(len(lst[0])):
            col = []
            for j in (lst):
                col.append(j[i])
            c.append(col)
        for j in range(len(c)):
            c[j].reverse()
        return c
    def counterclock(lst):
        c = []
        for i in range(len(lst[0])):
            col = []
            for j in (lst):
                col.append(j[i])
            c.append(col)
        c.reverse()
        return c
    if num<0:
        for i in range(-1*num):
            lst = counterclock(lst)
        return lst
    if num>0:
        for i in range(num):
            lst = clockwise(lst)
        return lst   
rotate_transform(lst,num)

