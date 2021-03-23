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

directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
rev_directions = {value: key for key, value in directions.items()}
​
def final_direction(initial, turns):
    direction = directions[initial]
    for turn in turns:
        if turn == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
    return rev_directions[direction]

