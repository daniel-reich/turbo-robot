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
  Paces = []
  
  for arg in steps:
    Paces.append(arg)
  
  if (Paces == []):
    return [0, 0]
  
  Horizontal = 0
  Vertical = 0
  
  Counter = 0
  Length = len(Paces)
  
  while (Counter < Length):
    
    Item = Paces[Counter]
    
    if (Counter % 4 == 0):
      Vertical += Item
      Counter += 1
    elif (Counter % 4 == 1):
      Horizontal += Item
      Counter += 1
    elif (Counter % 4 == 2):
      Vertical -= Item
      Counter += 1
    elif (Counter % 4 == 3):
      Horizontal -= Item
      Counter += 1
    else:
      Counter += 1
  
  Answer = []
  Answer.append(Horizontal)
  Answer.append(Vertical)
  
  return Answer

