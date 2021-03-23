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

def switch_gravity_on(lst):
    for x in range(len(lst[0])):
        count = 0
        for y in range(len(lst)):
            if lst[y][x]== '#':
                count += 1
        for i in range(len(lst)):
            if count>=1:
                lst[-1-i][x] = '#'
                count -=1
            else:
                lst[-1-i][x] = '-'
    return lst

