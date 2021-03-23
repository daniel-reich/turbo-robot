"""


Write a function that efficiently calculates Fibonacci terms.

### Examples

    fibonacci(1) ➞ 1
    
    fibonacci(2) ➞ 1
    
    fibonacci(4) ➞ 3
    
    fibonacci(64) ➞ 10610209857723

### Notes

The input will always be a power of two.

"""

memo = {1: 1, 2: 1}
​
def matrix_mult(A, B):
    C = [[0 for row in range(len(A))] for col in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C
​
A = [[1, 1], [1, 0]]
A = matrix_mult(A, A)
n = 2
while n < 10**6:
    A = matrix_mult(A, A)
    n *= 2
    f = A[0][1]
    memo[n] = f
​
def fibonacci(n):
    return memo[n]

