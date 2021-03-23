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
    if num > 0:
        partitions = []
        count = 0
        while count < num:
            for row in lst:
                partitions.append(row)
            partitions = partitions[::-1]
            temp = []
            for k in range(len(lst)):
                temp2 = []
                for i in range(len(lst)):
                    temp2.append(partitions[i][k])
                temp.append(temp2)
            lst = temp
            count += 1
        return lst
    else:
        count = 0
        while count > num:
            partitions = []
            for row in lst:
                partitions.append(row[::-1])
            temp = []
            for k in range(len(lst)):
                temp2 = []
                for i in range(len(lst)):
                    temp2.append(partitions[i][k])
                temp.append(temp2)
            lst = temp
            count -= 1
        return lst

