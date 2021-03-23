"""


The function is given a rectangular matrix consisting of zeros and ones. Count
the number of different regions and return the result. A separate region is a
collection of ones interconnected horizontally and vertically. A region can
have holes in it.

### Examples

    num_regions([
      [1, 1, 1, 1, 0],
      [1, 1, 0, 1, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0]
    ]) ➞ 1
    num_regions([
      [1, 1, 1, 1, 0],
      [1, 0, 0, 1, 0],
      [1, 1, 1, 1, 0],
      [0, 0, 0, 0, 1]
    ]) ➞ 2
    
    # The region on the upper left looks like a doughnut.
    num_regions([
      [1, 1, 0, 0, 0],
      [1, 1, 0, 0, 0],
      [0, 0, 1, 0, 1],
      [0, 0, 0, 1, 1]
    ]) ➞ 3

### Notes

N/A

"""

def num_regions(grid: list) -> int:
  ones = set((i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j])
  result = 0
  while len(ones) > 0:
    region = set([ones.pop()])
    while len(region) > 0:
      new_region = set()
      for a, b in region:
        for coords in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)):
          if coords in ones:
            new_region.add(coords)
            ones.remove(coords)
      region = new_region
    result += 1
  return result

