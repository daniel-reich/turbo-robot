"""


When a bug jumps to a `height` _y_ , its position can be plotted as a
quadratic function with _x_ as the `time`, and _y_ as the vertical distance
traveled. For example, for a bug that jumps 9 cm up and is back on the ground
after 6 seconds, its trajectory can be plotted as:

![bug jump quadratic plot](https://edabit-images.s3.amazonaws.com/2pMgjmZ.png)

Create a function that, given the max height of a vertical jump in cm and the
current time in milliseconds, returns the current position of the bug rounded
to two decimal places, and its direction (`"up"` or `"down"`). If the bug is
already back on the ground, return `0` for the position and `None` for the
direction.

### Examples

    bug_jump(9, 1000) ➞ [5, "up"]
    
    bug_jump(9, 4000) ➞ [8, "down"]
    
    bug_jump(9, 5500) ➞ [2.75, "down"]
    
    bug_jump(9, 7000) ➞ [0, None]

### Notes

  * Time and position both start at `0`.
  * You only need to translate the parabola (you don't need to scale it).

"""

def bug_jump(height, time):
    a=height**0.5*-2
    time=time/1000
    if(pos(time,a)<0):
        return[0,None]
    if(len(str(pos(time,a)))>9):
        return[round(pos(time,a),2),gradient(time,a)]
    return[pos(time,a),gradient(time,a)]
def gradient(x,a):
    if(x>-a):
        return None
    g= -2*x-a
    if(g==0):
        return None
    elif(g>0):
        return "up"
    else:
        return "down"
def pos(x,a):
    return -x**2-a*x

