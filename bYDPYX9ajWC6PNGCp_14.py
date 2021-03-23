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

def track_robot(*lst):
  movement = {0:"+y",1:"+x",2:"-y",3:"-x"}
  robot = [0,0]
  counter = 0
  for i in lst:
      if(movement[counter] == "+x"):
          robot[0]+=i
      elif(movement[counter] == "+y"):
          robot[1]+=i
      elif(movement[counter] == "-x"):
          robot[0]-=i
      elif(movement[counter] == "-y"):
          robot[1]-=i
      counter+=1
      if(counter>3):
          counter=0
  return robot

