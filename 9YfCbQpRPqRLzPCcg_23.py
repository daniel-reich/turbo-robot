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

def will_hit(equation, position):
    kvalue = equation.split()[2][0:-1]
    mvalue = equation.split()[3]+equation.split()[4]
    if (int(kvalue)*position[0]+int(mvalue)) == position[1]:
        return True
    else:
        return False

