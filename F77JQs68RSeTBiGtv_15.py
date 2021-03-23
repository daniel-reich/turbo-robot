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
  
  #   Building Diamond
  
  Diamond = []
  
  Number = 1
  Ceiling = n * n
  
  while (Number <= Ceiling):
    
    Batch = []
    Added = 0
    Required = n
    
    while (Added < Required):
      Batch.append(Number)
      Added += 1
      Number += 1
    
    Diamond.append(Batch)
  
  #   Bucket for Total
  Total = 0
  
  #   Going Down from Top Middle
  Cursor_A = int((n - 1) / 2)
  Cursor_B = int((n - 1) / 2)
  Row = 0
  
  while (Cursor_A >= 0):
    
    if (Cursor_A == Cursor_B):
      
      Value_A = Diamond[Row][Cursor_A]
      Total += Value_A
      
      Cursor_A -= 1
      Cursor_B += 1
      Row += 1
  
    else:
    
      Value_A = Diamond[Row][Cursor_A]
      Total += Value_A
      
      Value_B = Diamond[Row][Cursor_B]
      Total += Value_B
      
      Cursor_A -= 1
      Cursor_B += 1
      Row += 1
  
  #   Going Up from Bottom Middle
  Cursor_A = int((n - 1) / 2)
  Cursor_B = int((n - 1) / 2)
  Row = -1
  
  while (Cursor_A > 0):
    
    if (Cursor_A == Cursor_B):
      
      Value_A = Diamond[Row][Cursor_A]
      Total += Value_A
      
      Cursor_A -= 1
      Cursor_B += 1
      Row -= 1
  
    else:
    
      Value_A = Diamond[Row][Cursor_A]
      Total += Value_A
      
      Value_B = Diamond[Row][Cursor_B]
      Total += Value_B
      
      Cursor_A -= 1
      Cursor_B += 1
      Row -= 1
  
  #   Giving Answer
  return Total

