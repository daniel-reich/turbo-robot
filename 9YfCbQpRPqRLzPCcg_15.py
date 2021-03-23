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

def will_hit(formula,coordinate):
    formula_list = formula.split(" ")
    x_multi = formula_list[-3]
    digit = []
    
    
    #compute x
    if x_multi[0] == "-":
        for charac in range(1,(len(formula_list[-3])-1)):
            digit.append(x_multi[charac])
            final_x = float("".join(digit)) * -1 * coordinate[0]
    if x_multi[0] != "-":
        for charac in range(0,(len(formula_list[-3])-1)):
            digit.append(x_multi[charac])
            final_x = float("".join(digit)) * 1 * coordinate[0]
    
    
    #compute y
    if formula_list[-2] == "-":
        y_multi = -1 * float(formula_list[-1])
    
    if formula_list[-2] == "+":
        y_multi = 1 * float(formula_list[-1])
        
    if y_multi + final_x == coordinate[1]:
        return True
    else:
        return False
    
    return formula_list

