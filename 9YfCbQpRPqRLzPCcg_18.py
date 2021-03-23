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
  equation += ' '
  num = []
  sign = 1
  a = '' 
  for i in range(len(equation)):
    if equation[i].isdigit():
      a += equation[i]
      if equation[i-1] == '-':
        sign = -1
    elif i == len(equation)-1:
      num.append(int(a)*sign)
    elif len(num) != 0:
      if equation[i] == '-' or equation[i] == '+':
        num.append(equation[i])
    else:
      if len(a) != 0:
        num.append(int(a)*sign)
        sign = 1
        a = ''
  if num[1] == '+':
    num [1] = 1
  else: 
    num[1] = -1
  x = position[0]
  y = num[0]*x + num[1]*num[2]
  return y == position[1]

