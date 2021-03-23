"""


 **Mubashir** needs your help to identify the spread of a deadly virus. He can
provide you with the following parameters:

  * A two-dimensional array `persons`, containing **affected persons 'V'** and **unaffected persons 'P'**.
  * Number of hours `n`, each infected person is spreading the virus to one person _up, down, left and right_ **each hour**.

Your function should return the updated array containing affected and
unaffected persons after `n` hours.

### Examples

    persons = [
      ["P", "P", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    deadly_virus(persons, 0) ➞ [
      ["P", "P", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    
    deadly_virus(persons, 1) ➞ [
      ["V", "P", "P", "P", "P"],
      ["V", "V", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    
    deadly_virus(persons, 2) ➞ [
      ["V", "V", "P", "P", "P"],
      ["V", "V", "V", "P", "P"],
      ["V", "V", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]

### Notes

N/A

"""

def deadly_virus(grid, n):
    v_set, rows, cols = set(), len(grid), len(grid[0])
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v == "V":
                v_set.add((r, c))
    for _ in range(n):
        new_set = set()
        for p in v_set:
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r = p[0] + i
                c = p[1] + j
                if -1 < r < rows and -1 < c < cols:
                    new_set.add((r, c))
        v_set.update(new_set)
    res = [["P"] * cols for _ in range(rows)]
    for r, c in v_set:
        res[r][c] = "V"
    return res

