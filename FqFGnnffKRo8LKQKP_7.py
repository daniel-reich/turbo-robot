"""


 **Mubashir** needs your help to filter out **Simple Numbers** from a given
list.

### Simple Numbers

    89 = 8^1 + 9^2
    135 = 1^1 + 3^2 + 5^3

Create a function to collect these numbers from a given range between `a` and
`b` (both numbers are inclusive).

### Examples

    simple_numbers(1, 10) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    simple_numbers(1, 100) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
    
    simple_numbers(90, 100) ➞ []

### Notes

N/A

"""

############################################################
#     Sub Function
############################################################
​
def FNC_Simple_Number_Checker(Target):
​
  Power = 1
  Text = str(Target)
  Total = 0
  
  Counter = 0
  Length = len(Text)
  
  while (Counter < Length):
    Item = Text[Counter]
    Digit = int(Item)
    Score = Digit ** Power
    Total += Score
    Power += 1
    Counter += 1
  
  if (Total == Target):
    return True
  else:
    return False
  
​
############################################################
#     MAIN FUNCTION
############################################################
​
def simple_numbers(a, b):
​
  if (a <= b):
    Value = a
    Ceiling = b
  else:
    Value = b
    Ceiling = a
    
  Answer = []
  
  while (Value <= Ceiling):
    
    if FNC_Simple_Number_Checker(Value):
      Answer.append(Value)
      Value += 1
    else:
      Value += 1
  
  return Answer

