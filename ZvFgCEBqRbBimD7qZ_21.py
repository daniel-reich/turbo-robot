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
    i = 0
    total_score = 0
    frame = 1
    
    while frame<=10:
        
        #if its a strike
        if pins[i]==10:
            total_score = total_score+10+pins[i+1]+pins[i+2]
            frame+=1
            
        #if its a spare
        elif (pins[i] + pins[i+1])==10:
            total_score = total_score+10+pins[i+2]
            i+=1
            frame+=1
        
        elif (pins[i] + pins[i+1])<10:
            total_score = total_score+pins[i] + pins[i+1]
            i+=1
            frame+=1
            
        
        
        
        
        
        
        i+=1
    return total_score

