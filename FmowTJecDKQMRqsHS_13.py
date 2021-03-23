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

def crop_hydrated(f):
    for r in range(len(f)):
        for c in range(len(f[r])):
            if f[r][c] == "c":
                if not any([
                    f[r][min(c + 1, len(f[r]) - 1)] == "w",
                    f[r][max(c - 1, 0)] == "w",
                    f[min(r + 1, len(f) - 1)][c] == "w",
                    f[max(r - 1, 0)][c] == "w",
                    f[min(r + 1, len(f) - 1)][min(c + 1, len(f[r]) - 1)] == "w",
                    f[min(r + 1, len(f) - 1)][max(c - 1, 0)] == "w",
                    f[max(r - 1, 0)][min(c + 1, len(f[r]) - 1)] == "w",
                    f[max(r - 1, 0)][max(c - 1, 0)] == "w"
                    ]):
                        return False
                     
    return True

