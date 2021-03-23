"""


The function is given a map with `1` representing land, `0` representing
water. A land cell can have four neighbors along its edges. Compute the total
perimeter of shore-lines that are defined by land cells touching water or the
outer edges of the map. Each cell edge has a length equal to `1`. An isolated
cell without neighbors has a total perimeter length of `4`.

### Examples

    islands_perimeter([
      [0, 1, 0, 0],
      [1, 1, 1, 0],
      [0, 1, 0, 0],
      [1, 1, 0, 0]
    ]) ➞ 16
    islands_perimeter([
      [1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 0, 1, 1, 0, 1],
      [1, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1],
    ]), 42)
    islands_perimeter([
      [1, 0]
    ]) ➞ 4

### Notes

N/A

"""

def islands_perimeter(island):
  island = [[0]*(len(island[0])+2)]+[[0]+i+[0] for i in island]+[[0]*(len(island[0])+2)]
  get_neighbour = lambda y, x: [i for i in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)] if 0 <= i[1] < len(island[0]) and 0 <= i[0] < len(island) and not island[i[0]][i[1]]]
  return len(sum(sum([[get_neighbour(i, j) for j in range(len(island[i])) if island[i][j]] for i in range(len(island))], []), []))

