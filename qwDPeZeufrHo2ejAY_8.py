"""


Given a _string_ containing an _algebraic equation_ , calculate and **return
the value of x**. You'll only be given equations for simple **addition** and
**subtraction**.

### Examples

    eval_algebra("2 + x = 19") ➞ 17
    
    eval_algebra("4 - x = 1") ➞ 3
    
    eval_algebra("23 + 1 = x") ➞ 24

### Notes

  * There are spaces between every number and symbol in the string.
  * x may be a negative number.

"""

def eval_algebra(eq):
  words = eq.split()
  result = 0
  w0 = words[0]
  w1 = words[1] 
  w2 = words[2]
  w3 = words[3] 
  w4 = words[4]
  
  if w0 == "x" and w1 == "+":
    result = int(w4) - int(w2)
  elif w2 == "x" and w1 == "+":
    result = int(w4) - int(w0)
  elif w4 == "x" and w1 == "+":
    result = int(w0) + int(w2)
​
  elif w0 == "x" and w1 == "-":
    result = int(w4) + int(w2)
  elif w2 == "x" and w1 == "-":
    result = (int(w4) - int(w0)) * -1
  elif w4 == "x" and w1 == "-":
    result = int(w0) - int(w2)
​
  return result

