"""


Create a function which creates a square dartboard of side length `n`. The
value of a number should increase, the closer it is to the centre of the
board.

### Examples

    make_dartboard(3) ➞ [
      111,
      121,
      111
    ]
    
    make_dartboard(8) ➞ [
      11111111,
      12222221,
      12333321,
      12344321,
      12344321,
      12333321,
      12222221,
      11111111
    ]
    
    make_dartboard(5) ➞ [
      11111,
      12221,
      12321,
      12221,
      11111
    ]

### Notes

If the size given is an even number, the centre should be made up of the 4
highest values.

"""

def make_dartboard(n):
    '''
    Returns a square dartboard of side n as per the instructions
    '''
    def update_square(square, n, i, val):
        '''
        Updates square with the square derived from i
        '''
        for j in range(i, n-i):
            for k in range(i, n-i):
                square[j][k] = val
    
    square = [[1] * n for _ in range(n)]
    
    if n % 2 == 0:
        vals = list(range(2,n//2+1)) + list(range(n//2,1,-1))
    else:
        vals = list(range(2,n//2+2)) + list(range(n//2,1,-1))
    
    for i in range(1, n-1):
        update_square(square, n, i, vals[i-1])
​
    return [int(''.join([str(i) for i in row])) for row in square]

