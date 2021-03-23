"""


Given a 2D array of some suspended blocks (represented as hastags), return
another 2D array which shows the _end result_ once gravity is switched on.

### Examples

    switch_gravity_on([
      ["-", "#", "#", "-"],
      ["-", "-", "-", "-"],
      ["-", "-", "-", "-"],
      ["-", "-", "-", "-"]
    ]) ➞ [
      ["-", "-", "-", "-"],
      ["-", "-", "-", "-"],
      ["-", "-", "-", "-"],
      ["-", "#", "#", "-"]
    ]
    
    switch_gravity_on([
      ["-", "#", "#", "-"],
      ["-", "-", "#", "-"],
      ["-", "-", "-", "-"],
    ]) ➞ [
      ["-", "-", "-", "-"],
      ["-", "-", "#", "-"],
      ["-", "#", "#", "-"]
    ]
    
    switch_gravity_on([
      ["-", "#", "#", "#", "#", "-"],
      ["#", "-", "-", "#", "#", "-"],
      ["-", "#", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-", "-"]
    ]) ➞ [
      ["-", "-", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-", "-"],
      ["-", "#", "-", "#", "#", "-"],
      ["#", "#", "#", "#", "#", "-"]
    ]

### Notes

Each block falls individually, meaning there are no rigid objects. Think about
it like falling sand in Minecraft as opposed to the rigid blocks in Tetris.

"""

def switch_gravity_on(grid):
    number_of_obj = [0 for _ in range(len(grid[0]))]
    new_grid = [['-' for col in range(len(grid[row]))] for row in range(len(grid))]
​
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '#':
                number_of_obj[col] += 1
    
    for row in reversed(range(len(grid))):
        for col in range(len(grid[row])):
            if number_of_obj[col] > 0:
                new_grid[row][col] = '#'
                number_of_obj[col] -= 1
​
    return new_grid

