"""


Matt wants to make Rubik Cubes. These Rubiks should be in the shape of a full
cube, and it shouldn't have any missing parts.

This is a full cube:

![Full](https://edabit-challenges.s3.amazonaws.com/zauberwuerfel-geloest-
freshcuber900-300x300.jpg)

This is not a full cube:

![Full](https://edabit-challenges.s3.amazonaws.com/domino-cube.jpg)

And he asks his friend to draw some patterns. When his friend gives him these
Rubik's Cube patterns, he realizes that some of them are wrong or missing.
Help him identify them!

The small cubes that make up the Rubik's Cube will be denoted by "O".

  * Return `"Full"` if the Rubik Cube is full and no part is missing.
  * Return `"Non-Full"` if the Rubik Cube is non-full and no part is missing.
  * Return `"Missing {number of missing parts}"` if the Rubik Cube has missing parts.

### Examples

    identify(
      ["O", "O", "O"],
      ["O", "O", "O"],
      ["O", "O", "O"]
    ) ➞ "Full"
    
    # This is 3x3 full Rubik's Cube.
    # So we should return "Full"
    identify(
      ["O", "O", "O"],
      ["O", "O", "O"]
    ) ➞ "Non-Full"
    
    # This is a 2x3 Rubik's Cube.
    # It's not full, so we should return "Non-Full".
    identify(
      ["O", "O"],
      ["O", "O", "O"],
      ["O", "O", "O"]
    ) ➞ "Missing 1"
    
    # This is almost a 3x3 Rubik's Cube with one missing part.
    # We should return "Missing 1".

### Notes

  * Every cubic (small part of a Rubik's Cube) will be denoted by "O". There won't be any other type.
  * Don't forget to return by paying attention to capital letters.

"""

# 1-> find if cube is full or not, by checking len of cube vs len of current row.
​
# 2-> calculate the missing parts in current row, by deducting the longest len of row vs current row.
​
# 3-> if we have missing parts return it.
​
# 4-> if we don't have missing parts, but our len of cube is smaller than our longest row. then that means we have a non-full cube.
​
def identify(*cube):
  totalMissingParts = 0
  for row in range(len(cube)):
    maxLengthOfaRow = len(max([i for i in cube]))
    # Non-Full is True
    if len(cube) < maxLengthOfaRow or len(cube[row]) < maxLengthOfaRow:
      currentMissingParts = maxLengthOfaRow - len(cube[row])
      totalMissingParts += currentMissingParts
  
  if totalMissingParts:
    return "Missing {}".format(totalMissingParts)
  
  else:
    if len(cube) < maxLengthOfaRow and not totalMissingParts:
      return "Non-Full"
    else:
      return "Full"

