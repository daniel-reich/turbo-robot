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
  result = [0,0]
  tmp = [0,0,0,0]
  for i in instructions:
    d = i[0]
    v = int(i.split(" ")[1])
    print ("d :",d)
    print ("v : ",v)
    if d == 'r':
      tmp[0] += v
    if d == 'l':
      tmp[1] += v
    if d == 'u':
      tmp[2] += v
    if d == 'd':
      tmp[3] += v
​
  result[0] = tmp[0] - tmp[1]
  result[1] = tmp[2] - tmp[3]
  return result

