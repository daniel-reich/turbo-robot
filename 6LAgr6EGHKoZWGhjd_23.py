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

def final_direction(current, moves):
    compass = ["N", "E", "S", "W"]
    current_position = compass.index(current)
    count_moves = 0
    for move in moves:
        if move == "L":
            count_moves -= 1
        if move == "R":
            count_moves += 1
    if count_moves >= 0:
        net_moves = count_moves % 4
    elif count_moves < 0:
        net_moves = abs(count_moves) % 4
        net_moves = net_moves * -1
    gross_position = current_position + net_moves
​
    if gross_position > 3:
        return compass[gross_position - 4]
    if gross_position < 0:
        return compass[(len(compass))-abs(gross_position)]
    else:
        return compass[gross_position]

