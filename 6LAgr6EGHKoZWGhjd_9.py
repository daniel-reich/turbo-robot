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
  com = ["N", "E", "S", "W"]  # The directions on a compass in order
  overall_turn = 0
  initial_pos = com.index(initial)  # The position of the initial position
  
  for l in turns:  # Counting the tunrs
    if l == "R":
      overall_turn += 1
    else:
      overall_turn -= 1
    
  index = ((overall_turn + initial_pos) % 4)  # Using modulo to keep it in range and get the total displacement
  
  return com[index]

