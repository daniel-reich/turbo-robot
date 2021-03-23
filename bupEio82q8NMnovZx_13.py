"""


A robot has been given a list of movement instructions. Each instruction is
either `left`, `right`, `up` or `down`, followed by a distance to move. The
robot starts at `[0, 0]`. You want to calculate where the robot will end up
and return its final position as a list.

To illustrate, if the robot is given the following instructions:

    ["right 10", "up 50", "left 30", "down 10"]

It will end up 20 left and 40 up from where it started, so we return `[-20,
40]`.

### Examples

    track_robot(["right 10", "up 50", "left 30", "down 10"]) ➞ [-20, 40]
    
    track_robot([]) ➞ [0, 0]
    // If there are no instructions, the robot doesn't move.
    
    track_robot(["right 100", "right 100", "up 500", "up 10000"]) ➞ [200, 10500]

### Notes

  * The only instructions given will be `left`, `right`, `up` or `down`.
  * The distance after the instruction is always a positive whole number.

"""

def track_robot(instructions):
    x = 0
    y = 0
    result = [0,0]
    for i in range(len(instructions)):
        if instructions[i].split()[0] == 'right':
            x=x+int(instructions[i].split()[1])
        elif instructions[i].split()[0] == 'left':
            x=x-int(instructions[i].split()[1])
        elif instructions[i].split()[0] == 'up':
            y=y+int(instructions[i].split()[1])
        elif instructions[i].split()[0] == 'down':
            y=y-int(instructions[i].split()[1])
    return [x,y]

