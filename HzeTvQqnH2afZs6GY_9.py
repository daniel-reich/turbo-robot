"""


Create a function that takes in **size** and **direction** and generates a
**diagonal rug**.

The size is the `n` parameter, and all rugs are square `n x n`. The direction
is whether the diagonal part begins on the left or the right side.

### Examples

    generate_rug(4, "left") ➞ [
      [0, 1, 2, 3],
      [1, 0, 1, 2],
      [2, 1, 0, 1],
      [3, 2, 1, 0]
    ]
    
    generate_rug(5, "right") ➞ [
      [4, 3, 2, 1, 0],
      [3, 2, 1, 0, 1],
      [2, 1, 0, 1, 2],
      [1, 0, 1, 2, 3],
      [0, 1, 2, 3, 4]
    ]
    
    generate_rug(1, "left") ➞ [
      [0]
    ]
    
    generate_rug(2, "right") ➞ [
      [1, 0],
      [0, 1]
    ]

### Notes

  * `n > 0`
  * A `1 x 1` rug is trivially `[[0]]` (same for left and right).

"""

def generate_rug(n, direction):
    if n == 1:
        return [[0]]
    rug = []
    n2 = n // 2
    if direction == "left":
        rug = [list(range(n))]
        for r in range(1, n2):
            row = [0] * n
            start = r
            idx = start + 1
            k = 1
            while idx < n:
                row[idx] = k
                k += 1
                idx += 1
            idx = start - 1
            k = 1
            while idx >= 0:
                row[idx] = k
                k += 1
                idx -= 1
            rug.append(row)
        if n % 2 == 1:
            row = [0] * n
            for k in range(1, n2 + 1):
                row[n2 - k] = k
                row[n2 + k] = k
            rug.append(row)
            rug2 = rug[:-1]
            rug = rug + [row[::-1] for row in rug2[::-1]]
        else:
            rug = rug + [row[::-1] for row in rug[::-1]]
    else:
        rug = [list(range(n))[::-1]]
        for r in range(1, n2):
            row = [0] * n
            start = n - r - 1
            idx = start + 1
            k = 1
            while idx < n:
                row[idx] = k
                k += 1
                idx += 1
            idx = start - 1
            k = 1
            while idx >= 0:
                row[idx] = k
                k += 1
                idx -= 1
            rug.append(row)
        if n % 2 == 1:
            row = [0] * n
            for k in range(1, n2 + 1):
                row[n2 - k] = k
                row[n2 + k] = k
            rug.append(row)
            rug2 = rug[:-1]
            rug = rug + [row[::-1] for row in rug2[::-1]]
        else:
            rug = rug + [row[::-1] for row in rug[::-1]]                
    return rug

