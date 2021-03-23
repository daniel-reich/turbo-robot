"""


Create a function that takes an array of numbers, and returns the size of the
biggest square patch of odd numbers. See examples for a clearer picture.

### Examples

    odd_square_patch([
      [1, 2, 4, 9],
      [4, 5, 5, 7],
      [3, 6, 1, 7]
    ]) ➞ 2
    
    # The 2x2 square at the lower right
    # ([5, 7] on the 2nd row, [1, 7] on the third).
    
    odd_square_patch([[1, 2, 4, 9]]) ➞ 1
    
    # An array with a single row can only have a square patch of
    # maximum size 1x1 containing a single odd element.
    
    odd_square_patch([[2, 4, 6]]) ➞ 0

### Notes

N/A

"""

def check_Square(lst, posX, posY, w, h):
    try:
        # Iterate through every number in defined square
        y = 0
        while y < h:
            x = 0
            while x < w:
                # Return false if number is not false
                if lst[posY + y][posX + x] % 2 == 0:
                    return False
                x += 1
            y += 1
​
        return True
    except:
        return False
​
​
def odd_square_patch(lst):
    largestSquare = 0
​
    # Loop through every position in grid
    for y, row in enumerate(lst):
        for x, col in enumerate(row):
            # If number is not odd move to next
            if col % 2 == 0:
                continue
            # else iterate through squares with num as left top corner
            i = 0
            while True:
                check = check_Square(lst, x, y, 1 + i, 1 + i)
                if not check:
                    break
                elif i + 1 > largestSquare:
                    largestSquare = i + 1
                i += 1
​
    return largestSquare

