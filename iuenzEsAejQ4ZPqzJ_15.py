"""


This is a **reverse coding challenge**. Normally you're given explicit
directions with how to create a function. Here, you must generate your own
function to satisfy the relationship between the inputs and outputs.

Your task is to create a function that, when fed the inputs below, produce the
sample outputs shown.

### Examples

    3 ➞ 21
    
    9 ➞ 2221
    
    17 ➞ 22221
    
    24 ➞ 22228

### Notes

If you get stuck, check the **Comments** for help.

"""

def mystery_func(num):
  
  Answer = ""
  
  Target = num
  Score = 0
  
  Failsafe = 0
  
  while (Failsafe == 0):
    
    if (Score == 0) and (Score + 2 <= Target):
      Answer = Answer + "2"
      Score +=2
    elif (Score != 0) and (Score * 2 <= Target):
      Answer = Answer + "2"
      Score *= 2
    else:
      Failsafe += 1
    
  Remainder = Target - Score
  Answer = Answer + str(Remainder)
  Answer = int(Answer)
  
  return Answer

