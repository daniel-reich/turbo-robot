"""


You're given a 2D list / matrix of a crop field. Each crop needs a water
source. Each water source hydrates the 8 tiles around it. With `"w"`
representing a water source, and `"c"` representing a crop, is every crop
hydrated?

### Examples

    crop_hydrated([
      [ "w", "c" ],
      [ "w", "c" ],
      [ "c", "c" ]
    ]) ➞ True
    
    crop_hydrated([
      [ "c", "c", "c" ]
    ]) ➞ False
    # There isn"t even a water source.
    
    crop_hydrated([
      [ "c", "c", "c", "c" ],
      [ "w", "c", "c", "c" ],
      [ "c", "c", "c", "c" ],
      [ "c", "w", "c", "c" ]
    ]) ➞ False

### Notes

`"w"` on its own should return `True`, and `"c"` on its own should return
`False`.

"""

def crop_hydrated(arr):
    
    for x, i in enumerate(arr):
        for y, item in enumerate(i):
​
            if item != 'c':
                continue
​
            up = x != 0
            down = x != len(arr) - 1
            left = y != 0
            right = y != len(i) - 1
            
​
            # can go up
            if up:
                if arr[x-1][y] == 'w':
                    continue
            
            if down:
                if arr[x+1][y] == 'w':
                    continue
            
            if left:
                if arr[x][y-1] == 'w':
                    continue
            
            if right:
                if arr[x][y+1] == 'w':
                    continue
            
            if up and right:
                if arr[x-1][y+1] == 'w':
                    continue
            
            if up and left:
                if arr[x-1][y-1] == 'w':
                    continue
            
            if down and left:
                if arr[x+1][y-1] == 'w':
                    continue
            
            if down and right:
                if arr[x+1][y+1] == 'w':
                    continue
            
            return False
    return True

