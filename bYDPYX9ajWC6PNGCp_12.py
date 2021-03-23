"""


This robot roams around a 2D grid. It starts at `(0, 0)` facing North. After
each time it moves, the robot rotates 90 degrees clockwise. Given the amount
the robot has moved each time, you have to calculate the robot's final
position.

To illustrate, if the robot is given the movements `20, 30, 10, 40` then it
will move:

  * 20 steps North, now at `(0, 20)`
  * 30 steps East, now at `(30, 20)`
  * 10 steps South. now at `(30, 10)`
  * 40 steps West, now at `(-10, 10)`

...and will end up at coordinates `(-10, 10)`.

### Examples

    track_robot(20, 30, 10, 40) ➞ [-10, 10]
    
    track_robot() ➞ [0, 0]
    # No movement means the robot stays at (0, 0).
    
    track_robot(-10, 20, 10) ➞ [20, -20]
    # The amount to move can be negative.

### Notes

Each movement is an integer (whole number).

"""

def track_robot(*steps):
​
    #https://edabit.com/challenge/bYDPYX9ajWC6PNGCp
​
    steps = list(steps)
​
    Horizontal = []
    Vertical = []
​
    for ele in steps:
        if steps.index(ele) % 2 == 0:
            Vertical.append(ele)
        else:
            Horizontal.append(ele)
​
    Horizontal1 = []
​
    for ele in Horizontal:
        if Horizontal.index(ele) % 2 == 1:
            Horizontal1.append(ele*-1)
        else:
            Horizontal1.append(ele)
​
    Vertical1 = []
​
    for ele in Vertical:
        if Vertical.index(ele) % 2 == 1:
            Vertical1.append(ele * -1)
        else:
            Vertical1.append(ele)
​
    final = ([sum(Horizontal1)+0,sum(Vertical1)+0])
​
    return final

