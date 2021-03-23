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

def bowling_score(rolls):
    "Compute the total score for a player's game of bowling."
    if sum(rolls) == 0:
        return 0
    score, frame, roll_in_frame, pins_in_frame = 0, 1, 1, 0
    multiplier = [1] * len(rolls)
    for i in range(len(rolls)):
        roll = rolls[i]
        if frame < 10:
            if roll_in_frame == 1:
                # first roll of frame:
                if roll == 10:
                    # it's a strike, so double pins for next two balls
                    # (if there are such balls):
                    multiplier[i+1] += 1
                    multiplier[i+2] += 1
                    frame += 1
                    pins_in_frame = 0
                    roll_in_frame = 1
                else:
                    # not all pins knocked down with first roll in frame:
                    pins_in_frame = roll
                    roll_in_frame += 1
            elif roll_in_frame == 2:
                # second roll in frame (which, remember, is not last frame):
                if roll + pins_in_frame == 10:
                    # it's a spare:
                    multiplier[i+1] += 1
                frame += 1
                pins_in_frame = 0
                roll_in_frame = 1
        elif frame == 10:
            if roll_in_frame == 1:
                if roll == 10:
                    # a strike in last frame, so two bonus balls:
                    score += rolls[-2] + rolls[-1]
                else:
                    roll_in_frame += 1
                    pins_in_frame = roll
        else:
            assert False, "We should never reach this point!"
    #print multiplier
    score = sum([multiplier[i] *  rolls[i] for i in range(len(rolls))])
    return score
​
def bowling(pins):
    return bowling_score(pins)

