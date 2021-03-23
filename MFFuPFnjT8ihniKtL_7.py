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

def bug_jump(h, t):
    '''
    Returns the position of the bug after time t msecs, and its direction of
    travel as per instructions, given its maximum height is h cm.
    '''
    a, b, c = -1, 6, 0  # vanilla graph: y = -t^2 +6t
    v_max = 9  # h for the original graph, y coordinate of the vertex
    t /= 1000  # convert to secs
    k = 0      # for the horizontal translation
    mid = 3    # the x coordinate for the vanilla graph vertex
​
    if h != v_max:
        c = h - v_max  # the vertical translation
        x1 = (-b + (b*b - 4 * a * c)**0.5) / (2 * a)
        x2 = (-b - (b*b - 4 * a * c)**0.5) / (2 * a)
        k = min(abs(x1), abs(x2))  # lowest root
        
        if h < v_max:
            k = -k  # shifting left so add
​
    pos = round(-(t - k)**2 + b * (t - k) + c, 2)
    
    return [0, None] if pos < 0 else \
           [pos, 'up'] if t < mid + k else \
           [pos, 'down']

