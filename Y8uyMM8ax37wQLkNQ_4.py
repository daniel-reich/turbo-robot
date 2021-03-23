"""


Write a function that accepts an integer `n` and returns an `n * n` spiral
matrix.

### Examples

    matrix(2) ➞ [
      [1, 2],
      [4, 3]
    ]
    
    matrix(3) ➞ [
      [1, 2, 3],
      [8, 9, 4],
      [7, 6, 5]
    ]
    
    matrix(4) ➞ [
      [1,  2,  3,  4],
      [12, 13, 14, 5],
      [11, 16, 15, 6],
      [10,  9,  8, 7]
    ]

### Notes

In the examples, traverse the matrix in the clock-wise direction to observe
the spiral pattern.

"""

def spiralFill(m, n, a):  
    val = 1
    k, l = 0, 0
    while (k < m and l < n):  
        for i in range(l, n): 
            a[k][i] = val 
            val += 1
        k += 1
        for i in range(k, m): 
            a[i][n - 1] = val 
            val += 1
        n -= 1
        if (k < m): 
            for i in range(n - 1, l - 1, -1): 
                a[m - 1][i] = val 
                val += 1
            m -= 1
        if (l < n): 
            for i in range(m - 1, k - 1, -1): 
                a[i][l] = val 
                val += 1
            l += 1
def matrix(n):
    x=[]
    mat=[i for i in range(1,n*n+1)]
    b=[mat[i:i+n]for i in range(0,len(mat),n)]
    a = [[0 for j in range(n)] for i in range(n)] 
    spiralFill(n, n, a) 
    for i in range(n): 
        for j in range(n):
            x.append(a[i][j])           
    return[x[i:i+n]for i in range(0,len(x),n)]

