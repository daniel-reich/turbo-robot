"""


A brick in the shape of a cube sits on a heated surface capable of heating the
bottom of the brick to a constant temperature of 90 degrees. The air around
the brick is a constant 25 degrees. A perpendicular section through the center
of the brick is a `10x10` array showing the temperature at each of 100 points.

Let's specify that we can determine the temperature change of any point in the
array by averaging its temperature with the temperatures of its 8 contiguous
points (vertically, horizontally and diagonally). If the point is on the edge
or the corner of the array then some of those 8 points will be at the ambient
25 degrees.

Given that at time `t=0`, the bottom of the brick is at 90 degrees and the
rest of the brick is at the ambient 25 degrees, devise a function that will
calculate the array of temperatures at a later time `t` in minutes. You will
recalculate the temperatures at one minute intervals. Round them to the
nearest degree.

### Examples

    hot_brick(0) ➞ [
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
    ]
    
    hot_brick(1) ➞ [
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [39, 47, 47, 47, 47, 47, 47, 47, 47, 39]
      [90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
    ]
    
    hot_brick(10) ➞ [
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
      [25, 26, 26, 26, 26, 26, 26, 26, 26, 25]
      [26, 27, 28, 28, 28, 28, 28, 28, 27, 26]
      [28, 30, 32, 33, 33, 33, 33, 32, 30, 28]
      [31, 36, 39, 41, 41, 41, 41, 39, 36, 31]
      [38, 47, 51, 53, 54, 54, 53, 51, 47, 38]
      [50, 65, 69, 70, 71, 71, 70, 69, 65, 50]
      [90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
    ]

### Notes

  * Due to the symmetry of the problem, the array is always horizontally symmetrical.
  * Calculations at any time `t` are solely based on the previous time's `t-1` numbers.

"""

def hot_brick(t):
    br = [[25]*10 for _ in range(9)] + [[90]*10]
    for dt in range(t):
        brt = [[0]*10 for _ in range(9)] +[[90]*10]
        for r in range(9):
            for c in range(10):
                temp_sum = br[r][c]
                for dr, dc in [(0,1),(1,0),(1,1),(1,-1),(0,-1),(-1,0),(-1,-1),(-1,1)]:
                    y, x = r + dr, c + dc
                    temp_sum += br[y][x] if 0 <= y < 10 and 0 <= x < 10 else 25
                brt[r][c] = int(round(temp_sum / 9))
        br = brt
    return br

