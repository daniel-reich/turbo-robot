"""


You face 1 out of the 4 compass directions: `N`, `S`, `E` or `W`.

  * A **left turn** is a **counter-clockwise turn**. e.g. `N` (left-turn) ➞ `W`.
  * A **right turn** is a **clockwise turn**. e.g. `N` (right-turn) ➞ `E`.

Create a function that takes in a starting direction and a sequence of left
and right turns, and outputs the final direction faced.

### Examples

    final_direction("N", ["L", "L", "L"]) ➞ "E"
    
    final_direction("N", ["R", "R", "R", "L"]) ➞ "S"
    
    final_direction("N", ["R", "R", "R", "R"]) ➞ "N"
    
    final_direction("N", ["R", "L"]) ➞ "N"

### Notes

You can only face 1 out of the 4 compass directions: `N`, `S`, `E` or `W`.

"""

def final_direction(initial, turns):
  lst = ['N', 'E', 'S', 'W']
  turns = sum([1 if i == 'R' else -1 for i in turns])
  turns = lst.index(initial) + turns
  if turns >= 0:
    return lst[turns % 4]
  else:
    turns = -turns % 4
    return lst[-turns]

