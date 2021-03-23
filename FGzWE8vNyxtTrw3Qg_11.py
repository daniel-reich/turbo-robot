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

def find_coordinates(regions,coord):
    for i in regions:
        if coord in i:
            return True
    return False
​
def recursive_inspect(grid,coord,region):
​
    if grid[coord[0]][coord[1]] == 1 and coord not in region:
        region.add(coord)
    else:
        return region
​
    if coord[0] > 0 :
        recursive_inspect(grid,(coord[0]-1,coord[1]),region)
    if coord[1] < len(grid[coord[0]])-1:
        recursive_inspect(grid,(coord[0],coord[1]+1),region)
    if coord[0] < len(grid)-1:
        recursive_inspect(grid,(coord[0]+1,coord[1]),region)
    if coord[1] > 0 : 
        recursive_inspect(grid,(coord[0],coord[1]-1),region)
    return region
​
​
def num_regions(grid):
    i=0
    regions=[]
    region=set()
    
​
    while i < len(grid):
        j=0
        while j < len(grid[i]):
            if grid[i][j] == 1 and find_coordinates(regions,(i,j)) == False:
                regions.append(list(recursive_inspect(grid,(i,j),region)))
                region.clear()
            j+=1
        i+=1
​
    return len(regions)

