"""


 **Mubashir** has written a mysterious function that takes two numbers `a` and
`b` and returns _multiplication?_. Solve the riddle of what Mubashir's
function is by having a look at some of the examples below.

### Examples

    mubashir_function(0, 1) ➞ 0
    
    mubashir_function(1, 2) ➞ 2
    
    mubashir_function(10, 10) ➞ 1

### Notes

  * Check the **Tests** tab for more examples.
  * This isn't really a coding challenge, more of a fun riddle ;)

"""

def FNC_Digit_Totaller(Number):
​
  Text = str(Number)
  Total = 0
  
  Counter = 0
  Length = len(Text)
  
  while (Counter < Length):
    Item = Text[Counter]
    Digit = int(Item)
    Total += Digit
    Counter += 1
    
  return Total
​
def mubashir_function(a, b):
  
  Value_A = FNC_Digit_Totaller(a)
  Value_B = FNC_Digit_Totaller(b)
  
  Answer = Value_A * Value_B
  return Answer

