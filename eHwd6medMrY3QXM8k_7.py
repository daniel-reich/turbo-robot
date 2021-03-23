"""


Write a function that will return `True` if a given string (divided and
grouped into a size) will contain a set of **consecutive** numbers (regardless
of orientation: whether **ascending** or **descending** ), otherwise, return
`False`.

### Examples

    is_consecutive("121314151617") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 2's : 12, 13, 14, 15, 16, 17
    
    is_consecutive("123124125") ➞ True
    # Contains a set of consecutive ascending numbers
    # if grouped into 3's : 123, 124, 125
    
    is_consecutive("32332432536") ➞ False
    # Regardless of the grouping size, the numbers can't be consecutive.
    
    is_consecutive("326325324323") ➞ True
    # Contains a set of consecutive descending numbers
    # if grouped into 3's : 326, 325, 324, 323
    
    is_consecutive("667666") ➞ True
    # Consecutive descending numbers: 667 and 666.
    
    is_consecutive("999897959493") ➞ False

### Notes

  * A **number** can consist of any number of digits, so long as the numbers are **adjacent** to each other, and the string has **at least two** of them.
  * A **recursive** version of this challenge can be found via this [link](https://edabit.com/challenge/Ym27MyQQMRWGvEGeP).

"""

############################################################
#   Sub Function 1
############################################################
​
def FNC_Batch_Builder(Sample, Size):
​
  Blocks = []
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    
    Batch = ""
    Added = 0
    Required = Size
  
    while (Added < Required) and (Counter < Length):
      Item = Sample[Counter]
      Batch = Batch + Item
      Added += 1
      Counter += 1
    
    Number = int(Batch)
    Blocks.append(Number)
    Batch = ""
  
  if (Batch != ""):
    Number = int(Batch)
    Blocks.append(Number)
        
  return Blocks
​
############################################################
#   Sub Function 2
############################################################
​
def FNC_Consecutive_Up_Checker(Sample):
​
  First = 0
  Second = 1
  Length = len(Sample)
  
  while (Second < Length):
    
    Number_A = Sample[First]
    Number_B = Sample[Second]
    Difference = Number_B - Number_A
    
    if (Difference == 1):
      First += 1
      Second += 1
    else: 
      return False
  
  return True
​
############################################################
#   Sub Function 3
############################################################
​
def FNC_Consecutive_Down_Checker(Sample):
​
  First = 0
  Second = 1
  Length = len(Sample)
  
  while (Second < Length):
    
    Number_A = Sample[First]
    Number_B = Sample[Second]
    Difference = Number_A - Number_B
    
    if (Difference == 1):
      First += 1
      Second += 1
    else: 
      return False
  
  return True
​
############################################################
#   MAIN FUNCTION
############################################################
​
def is_consecutive(Sample):
​
  Testing = 1
  Ceiling = len(Sample)
  
  while (Testing < Ceiling):
    
    Blocks = FNC_Batch_Builder(Sample, Testing)
    
    if FNC_Consecutive_Up_Checker(Blocks):
      return True
    elif FNC_Consecutive_Down_Checker(Blocks):
      return True
    else:
      Testing += 1
      
  return False

