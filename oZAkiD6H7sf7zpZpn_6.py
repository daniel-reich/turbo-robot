"""


Create a function that takes two numbers and a mathematical operator and
returns the result.

### Examples

    calculate(4, 9, "+") ➞ 13
    
    calculate(12, 5, "-") ➞ 7
    
    calculate(6, 3, "*") ➞ 18
    
    calculate(25, 5, "//") ➞ 5
    
    calculate(14, 3, "%") ➞ 2
    
    calculate(7, 2, "/") ➞ 3.5

### Notes

  * Numbers can be negative.
  * The only operations used are those in the examples above.

"""

def calculate(num1, num2, operator):
    if operator == "+":
        return num1+ num2
    if operator == "-":
        return num1- num2
    if operator == "*":
        return num1* num2
    if operator == "//":
        return num1// num2
    if operator == "%":
        return num1% num2
    if operator == "/":
        return num1/ num2
print(calculate(4, 9, "+"))
print(calculate(12, 5, "-"))
print(calculate(6, 3, "*"))
print(calculate(25, 5, "//"))
print(calculate(14, 3, "%"))
print(calculate(7, 2, "/"))

