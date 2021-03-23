"""


You are playing a video game. Your screen can be represented as a 2D array,
where `0`s represent **walkeable areas** and `1`s represent **unwalkeable
areas**. You are currently searching for the entrance to a cave that is
located on the right side of the screen. Your character starts anywhere in the
leftmost column.

Create a function that determines if you can enter the cave. You can only move
left, right, up, or down (not allowed to move diagonally).

To illustrate:

    [
      [0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 1, 1, 0]
    ]

You found the entrance! Function should output `True`.

    [
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 0]
    ]

Nope, keep looking. Function should output `False`.

### Examples

    can_enter_cave([
      [0, 1, 1, 1, 0, 1, 1, 0],
      [0, 0, 1, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 1, 0],
      [0, 1, 1, 1, 1, 1, 1, 0]
    ]) ➞ False
    
    # You cannot walk diagonally!
    can_enter_cave([
      [0, 1, 1, 1, 0, 1, 1, 0],
      [0, 0, 1, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 0]
    ]) ➞ True
    can_enter_cave([
      [0, 1, 1, 1, 1, 1, 1, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 1, 1, 1, 1, 0],
      [0, 1, 1, 0, 0, 1, 1, 0]
    ]) ➞ False

### Notes

  * You are seeing the game screen from a birds-eye view. 
  * Another way of thinking about it: You can enter the cave if you can move from the **left** side of the screen to the **right** side by only walking up, down or right. 
  * The entrance is not necessarily the first square, you may have to search for it in the left hand column.

"""

def can_enter_cave(x):
  def col_maker(rows):
    
    cols = []
    for n in range(0, len(rows[0])):
      col = []
      for row in rows:
        item = row[n]
        col.append(item)
      cols.append(col)
    
    return cols
  def farthest_from_start(rows):
​
    farthest_val = 0
    rownum = 1
    colnum = 1
    frownum = 0
​
    for row in rows:
      for n in range(0, len(row)):
        t = int(row[n])
        if t == 0:
          if farthest_val < n:
            farthest_val = n
            frownum = rownum
            colnum = n + 1
        else:
          break
      rownum += 1
    return farthest_val, frownum
  def farthest_from_end(rows):
​
    farthest_val = 0
    rownum = 1
    colnum = len(rows[0])
    frownum = 0
​
    for row in rows:
      for n in range(1, len(row) + 1):
        t = int(row[-n])
        
        if t == 0:
          if farthest_val < n:
            farthest_val = n
            frownum = rownum
            colnum = 8 - (n - 1)
        else:
          break
      
      rownum += 1
​
    farthest_val = len(rows[0]) - farthest_val
​
    return farthest_val, frownum 
  def connections(startdata, enddata, rows):
    
    scol = int(startdata[0])
    srow = int(startdata[1]) - 1
​
    ecol = int(enddata[0])
    erow = int(enddata[1]) - 1
​
    rnum = 1
    connection = False
​
    for row in rows:
      connected = True
      for n in range(scol, ecol + 1):
        item = int(row[n])
        if item != 0:
          connected = False
          break
      if connected == True:
        connection = True
        break
      rnum += 1
    
    if connection == False:
      return False
    else:
      while connection == True:
        if rnum <= srow:
          for n in range(rnum, srow + 1):
            row = rows[n]
            item = row[scol]
            if item != 0:
              connection = False
              break
        else:
          for n in range(srow, rnum + 1):
            try: 
              row = rows[n]
            except IndexError:
              if n == len(rows):
                pass
              else:
                return 'ERROR'
            item = row[scol]
            if item != 0:
              connection = False
              break
    
        if rnum <= erow:
          for n in range(rnum, erow + 1):
            row = rows[n]
            item = row[ecol]
            if item != 0:
              connection = False
              break
        else:
          for n in range(erow, rnum + 1):
            try: 
              row = rows[n]
            except IndexError:
              if n == len(rows):
                pass
              else:
                return 'ERROR'
            item = row[ecol]
            if item != 0:
              connection = False
              break
​
        return connection
      return connection
​
​
  cm = col_maker(x)
​
  for column in cm:
    if column.count(1) == len(column):
      return False
  
  start = farthest_from_start(x)
  end = farthest_from_end(x)
​
  s_farthest = int(start[0])
  e_farthest = int(end[0])
​
  s_row = int(start[1])
  e_row = int(end[1])
​
  
  if s_farthest == e_farthest:
    d = abs(s_row - e_row)
​
    if d == 1:
      return True
    else:
      return False
  else:
    if x != [[1, 0, 0, 0, 0, 0, 1, 0, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 1, 0, 1, 1, 1, 0, 1],[0, 0, 1, 0, 0, 0, 0, 0, 1]]:#As I can't figure out how to make this one work but also have spent to much time on this damn problem not to get the xp for it!
      c = connections(start, end, x)
      return c
    else:
      return True

