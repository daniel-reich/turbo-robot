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
    total = 0
    throw = 0
    frame = 1
    while throw < len(pins):
        count = 1
        if count == 1:
            if pins[throw] == 10:
                #strike
                bonus = 'strike'
                if frame == 10:
                    total += 10 + pins[throw+1] + pins[throw+2]
                    break
                else:
                    try:
                        total += 10 + pins[throw+1] + pins[throw+2]
                    except:
                        try:
                            total += 10 + pins[throw+1]
                        except:
                            total += 10
                throw += 1
                frame += 1
            else:
                count += 1
                throw += 1
​
        if count == 2:
            if throw == len(pins):
                total += pins[throw-1]
            else:
                if pins[throw] + pins[throw-1] == 10:
                    #spare
                    bonus = 'spare'
                    if frame == 10:
                        total += 10 + pins[throw+1]
                        break
                    else:
                        try:
                            total += 10 + pins[throw+1]
                        except:
                            total += 10
                    throw += 1
                    frame += 1
                else:
                    #simple add
                    bonus = ''
                    total += pins[throw] + pins[throw-1]
                    throw += 1
                    frame += 1
    return total

