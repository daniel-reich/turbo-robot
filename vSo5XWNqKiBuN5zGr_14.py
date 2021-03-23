"""


Create a function that returns the **integral** part from the result of a
division between two numbers. This process of division can be achieved via
**repetitive subtraction** , thus, it can be done **recursively**.

### Examples

    divide(10, 2) ➞ 5
    
    divide(-51, -4) ➞ 12
    
    divide(3, 9) ➞ 0
    
    divide(-21, 5) ➞ -4
    
    divide(1024, 7) ➞ 146
    
    divide(273, -6) ➞ -45

### Notes

  * There will be no **zero-values** for the _divisor_.
  * You're expected to solve this challenge using a **recursive approach**.
  * You can read on more topics about recursion (see **Resources** tab) if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge.

"""

def divide(*args):
  
  Parameters = []
  
  for arg in args:
    Parameters.append(arg)
  
  if (len(Parameters) == 2):
    Parameters.append(0)
    Parameters.append(abs(Parameters[0]))
    Parameters.append(abs(Parameters[1]))
  
  Value_A = Parameters[0]
  Value_B = Parameters[1]
  Answer = Parameters[2]
  Remaining = Parameters[3]
  Divisor = Parameters[4]
​
  if (Remaining % Divisor != 0):
    Excess = Remaining % Divisor
    Remaining -= Excess
    return divide(Value_A, Value_B, Answer, Remaining, Divisor)
  
  elif (Value_A == 0):
    return Answer
  elif (Remaining == 0) and (Value_A > 0) and (Value_B > 0):
    return Answer
  elif (Remaining == 0) and (Value_A < 0) and (Value_B < 0):
    return Answer
  
  elif (Remaining == 0) and (Value_A > 0) and (Value_B < 0):
    return Answer * -1
  elif (Remaining == 0) and (Value_A < 0) and (Value_B > 0):
    return Answer * -1
    
  else:
    Remaining -= Divisor
    Answer += 1
    return divide(Value_A, Value_B, Answer, Remaining, Divisor)

