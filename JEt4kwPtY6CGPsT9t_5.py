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

def mathematical(exp, numbers):
  res = []
  exp = exp.replace("^","**")
  exp = exp.replace("x","*")
  var = exp[2]
  for num in numbers:
    exp_out = exp.replace(var,str(num))
    left,right = exp_out.split("=")
    ans = int(eval(right))
    res.append("%s=%s"%(left,ans))
  return res

