"""


Given an `nxn` grid of consecutive numbers, return the grid's **Diamond Sum**.
The diamond sum is defined as the sum of the numbers making up the diagonals
between adjacent sides.

### Examples

    diamond_sum(1) ➞ 1
    
    [1]
    diamond_sum(3) ➞ 20
    
    [
      [1, _, 3],
      [_, 5, _],
      [7, _, 9]
    ]
    
    # The numbers behind the underscores make up the Diamond Sum.
    # 2 + 4 + 6 + 8 = 20
    diamond_sum(5) ➞ 104
    
    [
      [1, 2, _, 4, 5],
      [6, _, 8, _, 10],
      [_, 12, 13, 14, _],
      [16, _, 18, _, 20],
      [21, 22, _, 24, 25]
    ]
    
    # 3 + 7 + 9 + 11 + 15 + 17 + 19 + 23 = 104

### Notes

  * `n` is always an **odd** number.
  * Bonus points for solving it mathematically!

"""

def diamond_sum(n):
    total = 0
    diamond_list = []
    row = []
    if n == 1:
        return 1
    for i in range(1, n*n + 1):
        row.append(i)
        if len(row) == n:
            diamond_list.append(row)
            row = []
    top_number = diamond_list[0][(n - 1)//2]
    bottom_number = diamond_list[n - 1][(n - 1)//2]
    total += top_number + bottom_number
    margin = 1
    for j in range(1, ((n - 1)//2)):
        total += diamond_list[j][((n - 1)//2) - margin] + diamond_list[j][((n - 1)//2) + margin]
        margin += 1
    total += diamond_list[(n - 1)//2][0] + diamond_list[(n - 1)//2][n - 1]
    new_margin = 1
    for k in range((((n - 1)//2) + 1), n - 1):
        total += diamond_list[k][0 + new_margin] + diamond_list[k][(n - 1) - new_margin]
        new_margin += 1
    return total

