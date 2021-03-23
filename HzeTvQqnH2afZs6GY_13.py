"""


Create a function that takes in **size** and **direction** and generates a
**diagonal rug**.

The size is the `n` parameter, and all rugs are square `n x n`. The direction
is whether the diagonal part begins on the left or the right side.

### Examples

    generate_rug(4, "left") ➞ [
      [0, 1, 2, 3],
      [1, 0, 1, 2],
      [2, 1, 0, 1],
      [3, 2, 1, 0]
    ]
    
    generate_rug(5, "right") ➞ [
      [4, 3, 2, 1, 0],
      [3, 2, 1, 0, 1],
      [2, 1, 0, 1, 2],
      [1, 0, 1, 2, 3],
      [0, 1, 2, 3, 4]
    ]
    
    generate_rug(1, "left") ➞ [
      [0]
    ]
    
    generate_rug(2, "right") ➞ [
      [1, 0],
      [0, 1]
    ]

### Notes

  * `n > 0`
  * A `1 x 1` rug is trivially `[[0]]` (same for left and right).

"""

def generate_rug(n, direction):
    '''
    Returns an n x n matrix withe the numbers 0 to n - 1 arranged diagonally
    as per direction, instructions above.
    '''
    numbers = [i for i in range(n-1,-1,-1)] + [i for i in range(1,n)]
    
    if direction == 'left':
        start = len(numbers) // 2  # start point for 1st row
        inc = -1   # direction of sliding window
        end = -1   # end of sliding window
    else:
        start = 0
        inc = 1
        end = n
​
    return [numbers[i : i + n] for i in range(start, end, inc)]

