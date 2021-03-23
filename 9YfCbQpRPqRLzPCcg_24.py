"""


In a video game, a meteor will fall toward the main character's home planet.
Given the meteor's trajectory as a string in the form **y = mx + b** and the
character's position as a tuple of `(x, y)`, return `True` if the meteor will
hit the character and `False` if it will not.

### Examples

    will_hit("y = 2x - 5", (0, 0)) ➞ False
    
    will_hit("y = -4x + 6", (1, 2)) ➞ True
    
    will_hit("y = 2x + 6", (3, 2)) ➞ False

### Notes

  * The **b** value will never be zero or blank.
  * The **m** value will always be an integer.
  * If the **m** value is 1, the "1" will be shown.
  * For example, "y = x + 5" will be shown as "y = 1x + 5".
  * If the **m** value is -1, the "-1" will be shown.
  * For example, "y = -x + 2" will be shown as "y = -1x + 2".

"""

import re
​
def will_hit(equation, position):
    equation = equation.replace(" ", "")
    y, x, c, = re.search(r"([-+]*\d*y)=([-+]*\d*x)([+-]*\d*)", equation).group(1, 2, 3)
    ysub = "*" + str(position[1]) if bool(re.search(r'\d', y)) else str(position[1])
    xsub = "*" + str(position[0]) if bool(re.search(r'\d', x)) else str(position[0])
​
    y = y.replace('y', ysub)
    x = x.replace('x', xsub)
​
    return eval(y) == eval(x+c)

