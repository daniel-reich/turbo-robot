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

def diamond_sum(num):
    if num == 1:
        return 1
​
    mid1 = (num + 1)  // 2
    mid2 = ((num ** 2 - num + 1) + (num ** 2)) // 2
    res = mid1 + mid2
​
    for i in range(num - 2):
        s = num + (num * i) + 1
        e = s + num - 1
        res = res + (s + e)
​
    return res

