"""


Some basic Python operators are `+`, `-`, `*`, `/`, and `%`. In this challenge
you will be given three parameters, `num1`, `num2`, and an `operator`. Use the
operator on number 1 and 2.

### Examples

    operate(1, 2, "+") ➞ 3
    # 1 + 2 = 3
    
    operate(7, 10, "-") ➞ -3
    # 7 - 10 = -3
    
    operate(20, 10, "%") ➞ 0
    # 20 % 10 = 0

### Notes

There will not be any divisions by zero.

"""

def operate(num1,num2,operator):
  if operator == "+":
    return num1 + num2
  elif operator == "/": 
    return num1 / num2
  elif operator == "*": 
    return num1 * num2
  elif operator == "%": 
    return num1 % num2
  elif operator == "-":
    return num1 - num2

