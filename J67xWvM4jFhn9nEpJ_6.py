"""


Make a function that takes a integer, `size`, returns 2D list that is a Magic
Square with side lengths of `size`

A Magic Square is an arrangement of numbers in a square in such a way that the
sum of each row, column, and diagonal is one constant number, the "magic
constant." For this challenge I will be testing with the assumption that your
magic squares are made with whole numbers from 1 - n^2

### Example

    make_magic(3) ➞ [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    # Rows: 2+7+6 = 9+5+1 = 4+3+8 = 15
    # Columns: 2+9+4 = 7+5+3 = 6+1+8 = 15
    # Diagonals: 2+5+8 = 6+5+4 = 15

### Notes

For this challenge I will only be testing with sizes >= 3 as there are no
Magic Squares of size 2 at least as I have described them.

"""

import numpy as np
import math
def build_sems(s):
    if s % 2 == 1:
        s += 1
    while s % 4 == 0:
        s += 2 
    q = [[0 for j in range(s)] for i in range(s)]
    z = s // 2
    b = z * z
    c = 2 * b
    d = 3 * b
    o = build_oms(z) 
    for j in range(0, z):
        for i in range(0, z):
            a = o[0][i][j]
            q[i][j] = a
            q[i + z][j + z] = a + b
            q[i + z][j] = a + c
            q[i][j + z] = a + d
 
    lc = z // 2
    rc = lc
    for j in range(0, z):
        for i in range(0, s):
            if i < lc or i > s - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = q[i][j]
                    q[i][j] = q[i][j + z]
                    q[i][j + z] = t 
    return q
def build_oms(s):
    if s % 2 == 0:
        s += 1
    q = [[0 for j in range(s)] for i in range(s)]
    p = 1
    i = s // 2
    j = 0
    while p <= (s * s):
        q[i][j] = p
        ti = i + 1
        if ti >= s: ti = 0
        tj = j - 1
        if tj < 0: tj = s - 1
        if q[ti][tj] != 0:
            ti = i
            tj = j + 1
        i = ti
        j = tj
        p = p + 1 
    return q    
def make_magic(size):
    n=size    
    if n%2==0:
        A=build_oms(n)
    else:    
        j,A=n//2,[[0]*n for i in[0]*n]
        i=c=0
        while c<n*n:c=A[i][j]=c+1;i,j=[i+1,[n,i][i>0]-1][c%n>0],[j,[n,j][j>0]-1][c%n>0]
    return A
def is_magic(size):
    arr=make_magic(size)    
    return is_magic_square(arr)

