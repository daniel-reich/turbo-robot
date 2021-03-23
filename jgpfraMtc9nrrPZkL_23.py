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

def fall(x,y,lst):
  lst[y][x] = "-"
  while (y+1 < len(lst) and lst[y+1][x] != "#"):
    y += 1
  lst[y][x] = "#"
​
def switch_gravity_on(lst):
  for y in range(len(lst)-1, -1, -1):
    for x in range(len(lst[0])):
      if (lst[y][x] == "#"):
        fall(x,y,lst)
  return lst

