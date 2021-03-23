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

def spiral_order(lst):
    result = []
    if len(lst) == 0:
        return []
    elif len(lst) == 1 and len(lst[0]) == 1:
        return [lst[0][0]]
    elif len(lst) == 1 and len(lst[0]) > 1:
        for j in range(len(lst[0])):
            result.append(lst[0][j])
        return result
    else:
        for j in range(len(lst[0])):
            result.append(lst[0][j])
        for i in range(1, len(lst) - 1):
            result.append(lst[i][-1])
        for j in range(len(lst[0]) - 1, -1, -1):
            result.append(lst[-1][j])
        for i in range(len(lst) - 2, 0, -1):
            result.append(lst[i][0])
        lst_remain = []
        for i in range(1, len(lst) - 1):
            lst_remain.append([lst[i][j] for j in range(1, len(lst[0]) - 1)])
    return result + spiral_order(lst_remain)

