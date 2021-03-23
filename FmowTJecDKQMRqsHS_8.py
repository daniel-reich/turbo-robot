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

def spreadWater(field, waterCoordinates):
    import numpy
    
    print(field)
    for water in waterCoordinates:
        for i in range(water[1] - 1, water[1] + 2):
            if i is not -1 and i < len(field[0]): 
                if field[water[0]][i] is not "w": 
                    field[water[0]][i] = '#'
                if water[0] is not 0:
                    if field[water[0] - 1][i] is not "w":
                        field[water[0] - 1][i] = '#'
                if water[0] < len(field) - 1:
                    if field[water[0] + 1][i] is not "w":
                        field[water[0] + 1][i] = '#'
    print(numpy.array(field))
    allWet = True
    for row in field:
        for tile in row:
            if tile is 'c':
                allWet = False
                break
    return allWet    
​
​
def crop_hydrated(field):
    waterCoordinates = []
    for row in range(len(field)):
        for tile in range(len(field[0])):
            if field[row][tile] is 'w':
                waterCoordinates.append((int(row), int(tile)))
    return spreadWater(field, waterCoordinates)

