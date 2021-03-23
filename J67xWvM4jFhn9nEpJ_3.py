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

# Make a magic square of side length n
​
def siamese(n):
  grid = []
  for i in range(n):
    row = [0 for x in range(n)]
    grid.append(row)
  x = n // 2 - 1
  y = 1
  for i in range(n**2):
    x += 1
    y -= 1
        
    if grid[y % n][x % n] != 0:
      y += 2
      x -= 1
​
    grid[y % n][x % n] = i + 1
  return grid
    
def crosses(n):
    grid = []
    for i in range(n):
        row = [x + 1 for x in range(i * n, (i + 1) * n)]
        grid.append(row)
​
    retval = []
    for i in range(n):
        retval.append([0]*n)
​
    for row in range(n):
        for col in range(n):
            if col % 4 + row % 4 == 3 or col % 4 == row % 4:
                retval[row][col] = grid[n - row - 1][n - col - 1]
            else:
                retval[row][col] = grid[row][col]
    return retval
​
def lux(n):
    m = (n - 2) // 4
    grid = []
    for i in range(m + 1):
        grid.append(['L']*(n // 2))
    grid.append(['U']*(n // 2))
    grid[-1][m] = 'L'
    grid[-2][m] = 'U'
    for i in range(m - 1):
        grid.append(['X']*(n // 2))
​
    retval = []
    for i in range(n):
        retval.append([0]*n)
​
    refgrid = siamese(n // 2)
​
    for row in range(n // 2):
        for col in range(n // 2):
            base = refgrid[row][col] - 1
            if grid[row][col] == 'L':
                retval[row * 2][col * 2 + 1] = 4 * base + 1
                retval[row * 2 + 1][col * 2] = 4 * base + 2
                retval[row * 2 + 1][col * 2 + 1] = 4 * base + 3
                retval[row * 2][col * 2] = 4 * base + 4
            elif grid[row][col] == 'U':
                retval[row * 2][col * 2] = 4 * base + 1
                retval[row * 2 + 1][col * 2] = 4 * base + 2
                retval[row * 2 + 1][col * 2 + 1] = 4 * base + 3
                retval[row * 2][col * 2 + 1] = 4 * base + 4
            else:
                retval[row * 2][col * 2] = 4 * base + 1
                retval[row * 2 + 1][col * 2 + 1] = 4 * base + 2
                retval[row * 2 + 1][col * 2] = 4 * base + 3
                retval[row * 2][col * 2 + 1] = 4 * base + 4
    return retval
    
def make_magic(n):
    if n % 2 == 1:
        return siamese(n)
    elif n % 4 == 0:
        return crosses(n)
    else:
        return lux(n)

