"""


Create a function that takes an expression `exp` and an upper limit `i` as
arguments and returns the sum of that expression up to the i'th term (recall
sigma from math class).

### Examples

    summation("n", 10) ➞ 55
    
    summation("1/n", 50) ➞ 4.5
    
    summation("n**n", 6) ➞ 50069

### Notes

  * Assume the lower limit is `i = 1`.
  * Round your answer to the nearest tenth.

"""

def summation(exp, i):
  
  Total = 0
  
  Cursor = 1
  End = i
  
  while (Cursor <= End):
    
    Equation = str(exp)
    New = str(Cursor)
    Equation = Equation.replace("n", New)
    Value = eval(Equation)
    Total += Value
    Cursor += 1
  
  Answer = round(Total,1)
  
  return Answer

