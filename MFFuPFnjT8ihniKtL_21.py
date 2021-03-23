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

def search_coefficients(height_max, time):
    a = -0.000001
    b = 0
    while a > -100:
        while b < 100:
            time_max = - b / (2 * a)
            if time_max > 0:
                height = a * time_max * time_max + b * time_max
                if height < height_max + 0.0001 and height >= height_max - 0.0001:
                    return a, b, time_max
            b += 0.00000001
        a -= 0.00000001
​
​
def bug_jump(height_max, time):
    where_fly = None
    a, b, time_max = search_coefficients(height_max, time)
    if time < 2 * time_max:
        if time > time_max:
            where_fly = 'down'
        else:
            where_fly = 'up'
    else:
        time = 0
    height = a * time * time + b * time
    height = round(height, 2)
    return [height, where_fly]

