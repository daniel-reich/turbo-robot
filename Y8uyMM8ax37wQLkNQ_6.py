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

def matrix(n):
    a=[[1for i in range(n)]for i in range(n)];b=n//2;i=1
    while n>b:
        if i>1:
            a[-n][-n] = a[-n][-1 - n]+1
        for j in range(i,n):
            a[-n][j] = a[-n][j - 1]+1
        for j in range ( i, n ):
            a[j][n - 1] = a[j - 1][n - 1]+1
        for j in range ( i, n ):
            a[n-1][- 1-j] = a[n - 1][- j]+1
        for j in range(i,n-1):
            a[-1-j][-n] = a[-j][-n]+1
        i+=1;n-=1
    return a

