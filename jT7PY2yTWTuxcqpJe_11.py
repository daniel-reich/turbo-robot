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
    k = 0
    l = 0
    x=[]
    m=len(arr)
    n=len(arr[0])
    while (k < m and l < n):
        for i in range(l, n):
            x.append(arr[k][i])
        k+=1
        for i in range(k, m):
            x.append(arr[i][n - 1])
        n-=1
        if (k < m): 
            for i in range(n - 1, (l - 1), -1):
                x.append(arr[m - 1][i])
            m-=1
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                x.append(arr[i][l] )
            l+=1
    return x

