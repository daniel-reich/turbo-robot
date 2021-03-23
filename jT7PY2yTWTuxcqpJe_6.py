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

def spiral_order(arr):
    d = ['R', 'D', 'L', 'U']
    res = []
    
    while arr:
        if d[0] == 'R':
            res += arr.pop(0)
        elif d[0] == 'D':
            res += [i.pop() for i in arr]
        elif d[0] == 'L':
            res += arr.pop()[::-1]
        else:
            res += [i.pop(0) for i in arr][::-1]
        d = d[1:] + d[:1]
    return res

