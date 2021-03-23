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
  return [list(z) for z in zip(*[sorted(l)[::-1] for l in zip(*lst)])]

