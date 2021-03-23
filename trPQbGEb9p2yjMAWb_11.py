"""


In this challenge, you have to verify that every, or some, of the given
variables, pass a given test condition. There are seven parameters:

  * `test`: A string being the condition to verify.
  * `val`: A string with two possible values:
    * `everybody` if **every** variable has to pass the test;
    * `somebody` if **at least one** of the variables has to pass the test.
  * `a`, `b`, `c`, `d`, `e`: The variables being integers or booleans.

Create a function that returns `True` or `False`, depending on the result of
the test applied to the variables.

### Examples

    every_some(">= 1", "everybody", 1, 1, -1, 1, 1) ➞ False
    # Is every variable >= 1?
    
    every_some(">= 1", "somebody", -1, -1, -1, -1, 1) ➞ True
    # Is some variable >= 1?
    
    every_some("< 4 / 2", "everybody", 1, 2, 1, 0, -10) ➞ False
    # Is every variable < 2?

### Notes

N/A

"""

def every_some(test, val, a, b, c, d, e):
  
  Sentence_A = str(a) + str(test)
  Test_A = eval(Sentence_A)
  
  Sentence_B = str(b) + str(test)
  Test_B = eval(Sentence_B)
  
  Sentence_C = str(c) + str(test)
  Test_C = eval(Sentence_C)
  
  Sentence_D = str(d) + str(test)
  Test_D = eval(Sentence_D)
  
  Sentence_E = str(e) + str(test)
  Test_E = eval(Sentence_E)
  
  Events = 0
  
  if (Test_A):
    Events += 1
  elif (Test_B):
    Events += 1
  elif (Test_C):
    Events += 1
  elif (Test_D):
    Events += 1
  elif (Test_E):
    Events += 1
    
  if (val == "everybody") and (Events == 5):
    return True
  elif (val == "somebody") and (Events > 0):
    return True
  else:
    return False

