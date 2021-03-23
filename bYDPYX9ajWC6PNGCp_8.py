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

def track_robot (*steps):
    x=y=xs=ys=0
    for s in range(len(steps)):
        if s%2==0:
            if ys%2==0:
                y+=steps[s]
            else:
                y-=steps[s]
            ys+=1
        else:
            if xs%2==0:
                x+=steps[s]
            else:
                x-=steps[s]
            xs+=1
    return [x,y]

