"""


An **island is a region of contiguous ones**. A contiguous one is a `1` that
is touched by at least one other `1`, either **horizontally** , **vertically**
or **diagonally**. Given a piece of the map, represented by a 2-D list, create
a function that returns the area of the largest island.

To illustrate, if we were given the following piece of the map, we should
return `4`.

    [
      [0, 0, 0],
      [0, 1, 1],
      [0, 1, 1]
    ]

Our function should yield `2` for the map below:

    [
      [1, 0, 0],
      [0, 0, 1],
      [0, 0, 1]
    ]

Our function should yield `4` for the map below: :

    [
      [1, 0, 0],
      [0, 1, 1],
      [0, 0, 1]
    ]

### Examples

    largest_island([
      [1, 0, 0], 
      [0, 0, 0], 
      [0, 0, 1]
    ])
    
    ➞ 1
    
    largest_island([
      [1, 1, 0], 
      [0, 1, 1], 
      [0, 0, 1]
    ])
    
    ➞ 5
    
    largest_island([
      [1, 0, 0], 
      [1, 0, 0], 
      [1, 0, 1]
    ])
    
    ➞ 3

### Notes

  * Maps can be any `m x n` dimension.
  * Maps will always have at least 1 element. `m >= 1` and `n >= 1`.

"""

def largest_island(lst):
  largest = 0
  seen = []
  
  for y in range(len(lst)):
    for x in range(len(lst[0])):
      if lst[y][x] == 1 and [y, x] not in seen:
        to_check = [[y, x]]
        seen.append([y, x])
        current_count = 1
        while to_check:
          y = to_check[0][0]
          x = to_check [0][1]
          del to_check[0]
          pointer_y = y + 1
          while pointer_y < len(lst) and lst[pointer_y][x] == 1 and [pointer_y, x] not in seen:
            to_check.append([pointer_y, x])
            seen.append([pointer_y, x])
            current_count += 1
            pointer_y += 1
          pointer_x = x + 1
          while pointer_x < len(lst[y]) and lst[y][pointer_x] == 1 and [y, pointer_x] not in seen:
            to_check.append([y, pointer_x])
            seen.append([y, pointer_x])
            current_count += 1
            pointer_x += 1
          pointer_y, pointer_x = y+1, x+1
          while pointer_x < len(lst[y]) and pointer_y < len(lst) and lst[pointer_y][pointer_x] == 1 and [pointer_y, pointer_x] not in seen:
            to_check.append([pointer_y, pointer_x])
            seen.append([pointer_y, pointer_x])
            current_count += 1
            pointer_y += 1
            pointer_x += 1
          pointer_y, pointer_x = y+1, x-1
          while pointer_x >=0 and pointer_y < len(lst) and lst[pointer_y][pointer_x] == 1 and [pointer_y, pointer_x] not in seen:
            to_check.append([pointer_y, pointer_x])
            seen.append([pointer_y, pointer_x])
            current_count += 1
            pointer_y += 1
            pointer_x -= 1
        largest = max(current_count, largest)
  
  return largest

