"""


Create a function that returns a number which can block the player from
reaching 3 in a row in a game of Tic Tac Toe. The number given as an argument
will correspond to a grid of Tic Tac Toe: topleft is 0, topright is 2,
bottomleft is 6, and bottomright is 8.

  * Create a function that takes two numbers `a`, `b` and returns another number.
  * This number should be the final one in a line to block the player from winning.

### Examples

    block_player(0, 3) ➞ 6
    
    block_player(0, 4) ➞ 8
    
    block_player(3, 5) ➞ 4

### Notes

The values given will always have two filled squares in a line.

"""

def block_player(a, b):
​
    if abs(a-b) == 2 or abs(a-b) == 6 or (a+b) == 8: return (a+b) // 2
​
    if abs(a-b) == 3:
        if max(a, b) in [3, 4, 5]: return max(a, b) + 3
        else: return min(a, b) - 3
​
    if abs(a - b) == 4:
        if max(a, b) == 4: return 4 + 4
        else: return 0
​
    if abs(a - b) == 1:
        if (a + b) % 3 ==0: return min(a, b) - 1
        else: return max(a, b) + 1
    if abs(a - b) == 1:
        if (a + b) % 3 ==0:
            return min(a, b) - 1
        else:
            return max(a, b) + 1

