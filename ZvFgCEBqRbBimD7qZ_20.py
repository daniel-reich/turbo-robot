"""


Tenpin bowling scores can range from 0 (all gutter balls) to 300 (a perfect
game). If you are unfamiliar with scorekeeping, please see the **Resource**
for a quick description.

A complete record of a 10 frame bowling game can be given as a list of the
number of pins knocked down by each ball in sequence from beginning to the end
of the game.

Create a function whose argument is such a list. The function should return
the final score.

### Examples

    bowling([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) ➞ 300
    
    bowling([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]) ➞ 80
    
    bowling([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) ➞ 150
    
    bowling([10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10]) ➞ 200

### Notes

The number of balls thrown for a complete game can vary from 11 to 21
depending on the number of strikes thrown.

"""

def bowling(pins):
    score = 0
    frame = 1
    throw = 0
    for index, _ in enumerate(pins):
        throw += 1
        if throw == 1 and pins[index] == 10:
            if index < len(pins) - 2:
                score = score + 10 + pins[index + 1] + pins[index + 2]
                throw = 0
                frame += 1
            else:
                throw = 0
                frame += 1
        elif throw == 2:
            if pins[index] + pins[index - 1] == 10:
                score = score + 10 + pins[index + 1]
                throw = 0
                frame += 1
            else:
                score = score + pins[index] + pins[index - 1]
                throw = 0
                frame += 1
    return score

