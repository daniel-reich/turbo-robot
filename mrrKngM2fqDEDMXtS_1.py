"""


A broken bridge can be represented by `1`s and `0`s, where contiguous `0`s
represent holes. You can walk across a bridge with a hole with a maximum width
of 1, but any holes bigger than that you must fix first. For example, the
bridge below is walkeable:

    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1]

This bridge is not:

    [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

You own several wooden planks, each with different widths. You can patch the
holes on the bridge with these planks. More specifically, a plank size `n` can
fill a `n`-sized hole. If you had a plank of size `2`, the un-walkeable bridge
above could be filled in:

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

But even if you only had a plank of size `1`, you could still transform the
unwalkeable bridge into a walkeable one:

    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

Write a function that takes in a broken bridge, a list of plank sizes, and
returns `True` if the bridge can be patched up enough to walk over, and
`False` otherwise.

### Examples

    can_patch([1, 0, 0, 0, 0, 0, 0, 1], [5, 1, 2]) ➞ True
    # You can use the 5 plank to transform the 6 hole to a 1 hole.
    # Leftover planks [1, 2] are okay.
    
    can_patch([1, 0, 0, 0, 0, 0, 0, 1], [4, 1, 2, 3, 4]) ➞ False
    # None of your planks are long enough (you can't combine them).
    
    can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 2]) ➞ True
    
    can_patch([1, 0, 0, 1, 1, 0, 0, 0, 1], [1, 1]) ➞ False

### Notes

  * Individual planks may NOT be combined to form a longer plank.
  * Leftover planks are okay.

"""

def can_patch(bridge, planks):
  holes = []
  boards = planks
  counter = -1
  while counter < len(bridge) - 1:
    counter += 1
    if bridge[counter] == 0:
      var = counter
      while bridge[counter] == 0:
        counter += 1
      holes.append(bridge[var:counter])
  for hole in holes:
    if len(hole) == 1:
      continue
    if boards == []:
      return False
    for x in range(len(boards)):
      if boards[x] == len(hole) or boards[x] == len(hole) - 1:
        boards.pop(x)
        break
      if x == len(boards) - 1:
        return False
  return True

