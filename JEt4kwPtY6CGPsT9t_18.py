"""


Create a function that takes a mathematical expression as a string, list of
numbers on which the mathematical expression is to be calculated and return
the result as a list of string.

### Examples

    mathematical("f(y)=y+1",[1,2]) ➞ ["f(1)=2","f(2)=3"]
    
    mathematical("f(y)=y^2",[1,2,3]) ➞ ["f(1)=1","f(2)=4","f(3)=9"]
    
    mathematical("f(y)=yx3",[1,2,3]) ➞ ["f(1)=3","f(2)=6","f(3)=9"]

### Notes

  * List of numbers are positive integers.
  * In the algebraic expression x = `*`

"""

def solve(exp):
    if "+" in exp:
        return str(int(exp.split("+")[0]) + int(exp.split("+")[1]))
    elif "-" in exp:
        return str(int(exp.split("-")[0]) - int(exp.split("-")[1]))
    elif "/" in exp:
        return str(int(int(exp.split("/")[0]) / int(exp.split("/")[1])))
    elif "x" in exp:
        return str(int(exp.split("x")[0]) * int(exp.split("x")[1]))
    else:
        return str(int(exp.split("^")[0]) * int(exp.split("^")[0]))        
def mathematical(exp, numbers):
    outputarr = [exp.split("=")[0].replace("y", str(number)) + "=" + solve(exp.split("=")[1].replace("y", str(number))) for number in numbers]
    return outputarr

