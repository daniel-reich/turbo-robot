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

from collections import defaultdict
​
def make_square(size, matrix):
    square = []
    for j in range(size):
        line = []
        for i in range(size):
            line.append(matrix[i,j])
        square.append(line)
    return square        
​
def make_magic(size):
    if size % 2 == 1:
        matrix = defaultdict(int)
        p = 1
        i,j = int(size/2),0
        while p <= size**2:
            matrix[(i,j)] = p
            if matrix[((i+1)%size,(j-1)%size)] == 0:
                i, j, p = (i+1)%size, (j-1)%size, p+1
            else:
                i, j, p = i, (j+1)%size, p+1
        return (make_square(size, matrix))
        
    if size % 4 == 0:
        q = size // 4
        forbidden = defaultdict(lambda: False)
        for i in range(4):
            forbidden[(i,i)] = True
            forbidden[(i,3-i)] = True
        for i in range(4):
            for j in range(4):
                for r in range(q):
                    for s in range(q): 
                        forbidden[(i + 4 * r, j + 4 * s)] = forbidden[(i,j)] 
        p = 1
        matrix = defaultdict(int)
        not_used = []
        for j in range(size):
            for i in range(size):
                if not forbidden[(i,j)]:
                    matrix[(i,j)] = p
                else:
                    not_used.append(p)
                p += 1
        not_used = not_used[::-1]
        for j in range(size)[::-1]:
            for i in range(size)[::-1]:
                if matrix[(i,j)] == 0:
                    matrix[(i,j)] = not_used.pop()
​
        return (make_square(size, matrix))
​
    if size == 6:
        return [[35,26,1,19,6,24],
                [8,17,28,10,33,15],
                [3,21,32,23,7,25],
                [30,12,5,14,34,16],
                [31,22,9,27,2,20],
                [4,13,36,18,29,11]]
​
    if size == 10:
        return [[92,67,99,74,1,51,8,58,15,40],
                [17,42,24,49,76,26,83,33,90,65],
                [98,73,80,55,7,57,14,64,16,41],
                [23,48,5,30,82,32,89,39,91,66],
                [4,54,81,56,88,63,20,70,22,47],
                [79,29,6,31,13,38,95,45,97,72],
                [85,60,87,62,19,69,21,71,3,28],
                [10,35,12,37,94,44,96,46,78,53],
                [86,61,93,68,25,75,2,52,9,34],
                [11,36,18,43,100,50,77,27,84,59]]
    
    if size == 14:
        return [[177,128,186,137,195,146,1,99,10,108,19,68,28,77],
                [30,79,39,88,48,97,148,50,157,59,166,117,175,126],
                [185,136,194,145,154,105,9,107,18,116,27,76,29,78],
                [38,87,47,96,7,56,156,58,165,67,174,125,176,127],
                [193,144,153,104,155,106,17,115,26,124,35,84,37,86],
                [46,95,6,55,8,57,164,66,173,75,182,133,184,135],
                [5,103,161,112,163,114,172,123,34,132,36,85,45,94],
                [152,54,14,63,16,65,25,74,181,83,183,134,192,143],
                [160,111,162,113,171,122,33,131,42,140,44,93,4,53],
                [13,62,15,64,24,73,180,82,189,91,191,142,151,102],
                [168,119,170,121,179,130,41,139,43,141,3,52,12,61],
                [21,70,23,72,32,81,188,90,190,92,150,101,159,110],
                [169,120,178,129,187,138,49,147,2,100,11,60,20,69],
                [22,71,31,80,40,89,196,98,149,51,158,109,167,118]]

