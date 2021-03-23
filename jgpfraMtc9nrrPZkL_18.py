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
    gravityOn = [['-' for i in range(len(lst[0]))] for x in range(len(lst))]
    for column in range(len(lst[0])):
        blockCount = 0
        for tile in range(len(lst)):
            if lst[tile][column]  is '#':
                blockCount += 1
        for block in range(blockCount):
            gravityOn[0 - (block + 1)][column] = '#'
    return gravityOn

