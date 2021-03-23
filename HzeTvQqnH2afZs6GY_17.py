"""


Create a function that takes in **size** and **direction** and generates a
**diagonal rug**.

The size is the `n` parameter, and all rugs are square `n x n`. The direction
is whether the diagonal part begins on the left or the right side.

### Examples

    generate_rug(4, "left") ➞ [
      [0, 1, 2, 3],
      [1, 0, 1, 2],
      [2, 1, 0, 1],
      [3, 2, 1, 0]
    ]
    
    generate_rug(5, "right") ➞ [
      [4, 3, 2, 1, 0],
      [3, 2, 1, 0, 1],
      [2, 1, 0, 1, 2],
      [1, 0, 1, 2, 3],
      [0, 1, 2, 3, 4]
    ]
    
    generate_rug(1, "left") ➞ [
      [0]
    ]
    
    generate_rug(2, "right") ➞ [
      [1, 0],
      [0, 1]
    ]

### Notes

  * `n > 0`
  * A `1 x 1` rug is trivially `[[0]]` (same for left and right).

"""

def generate_rug(n, direction):
    res = []
    if n == 1: return [[0]]
    if direction == 'left':
        tempLst = []
        res = []
        for col in range(n):
            tempLst.append(col)
        res.append(tempLst)
        tempLst = []
        col = 0
        row = 1
        while True:
            if col >= n:
                res.append(tempLst)
                tempLst = []
                row += 1
                col = 0
                tempLst.append(res[row - 1][0] + 1)
                if row == n and col == 0: break
                col += 1
            else:
                if col == 0:
                    tempLst.append(row)
                    col += 1
                tempLst.append(res[row -1][col - 1])
                col += 1
    else:
        tempLst = []
        res = []
        for col in range(n):
            tempLst.append(n - col - 1)
        res.append(tempLst)
        tempLst = []
        col = 0
        row = 1
        while True:
            if col >= n - 1:
                tempLst.append(row)
                res.append(tempLst)
                tempLst = []
                row += 1
                col = 0
                if row == n: break
            else:
                if col == n - 1:
                    tempLst.append(row - 1)
                    res.append(tempLst)
                    tempLst = []
                    col = 0
                    row += 1
                    if row == n: break
                tempLst.append(res[row - 1][col + 1])
                col += 1
    return res

