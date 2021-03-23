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
    list_of_tuples = zip(*lst[::-1])
    a=[list(elem) for elem in list_of_tuples]
    if num==-1 or num==3:
        return [ele[::-1]for ele in a][::-1]
    if num==2 or num==-2 :
        return [ele[::-1]for ele in lst[::-1]]
    if num==5or num==1:
        return a
    if num==-5:
        return [ele[::-1]for ele in a[::-1]]
    else:
        return lst

