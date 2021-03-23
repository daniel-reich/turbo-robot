"""


Given a matrix of m * n elements (m rows, n columns), return all elements of
the matrix in spiral order.

### Examples

    spiral_order([
      [ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ]
    ]) ➞ [1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    spiral_order([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]) ➞ [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

### Notes

NA

"""

def spiral_order(mat):
    def right():
        nonlocal mat, i, j, num, res
        while j+1 < col and num >= 1 and mat[i][j+1] != '-':
            res.append(mat[i][j+1])
            mat[i][j+1] = '-'
            j += 1
            num -= 1
    def down():
        nonlocal mat, i, j, num, res
        while i+1 < row and num >= 1 and mat[i+1][j] != '-':
            res.append(mat[i+1][j])
            mat[i+1][j] = '-'
            i += 1
            num -= 1
    def left():
        nonlocal mat, i, j, num, res
        while j-1 >= 0 and num >= 1 and mat[i][j-1] != '-':
            res.append(mat[i][j-1])
            mat[i][j-1] = '-'
            j -= 1
            num -= 1
    def up():
        nonlocal mat, i, j, num, res
        while i-1 > 0 and num >= 1 and mat[i-1][j] != '-':
            res.append(mat[i-1][j])
            mat[i-1][j] = '-'
            i -= 1
            num -= 1
    def seq():
        nonlocal i, j, cnt
        while num >= 1:
            right()
            down()
            left()
            up()
            cnt += 1
​
    row = len(mat); col = len(mat[0]); num = row*col-1
    i = 0; j  = 0; cnt = 0; res = [mat[i][j]]
    seq()
    return res

