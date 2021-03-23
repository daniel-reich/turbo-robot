"""


Create a function which counts how many lone `1`s appear in a given number.
Lone means the number doesn't appear twice or more in a row.

### Examples

    count_lone_ones(101) ➞ 2
    
    count_lone_ones(1191) ➞ 1
    
    count_lone_ones(1111) ➞ 0
    
    count_lone_ones(462) ➞ 0

### Notes

Tests will include positive whole numbers only.

"""

def count_lone_ones(n):
  
  Text = str(n)
  
  if (n == 1):
    return 1
  
  elif (n >= 10) and (n <= 19) and (n != 11):
    return 1
  
  elif (Text[-1] == "1") and (n > 20) and (n < 100):
    return 1
  
  else:
    Lonely = 0
    Start = 0
    End = 3
    Length = len(Text)
    
    while (End < Length):
      
      Block = Text[Start:End]
      
      if (Block[0] != "1") and (Block[1] == "1") and (Block[2] != "1"):
        Lonely += 1
        Start += 1
        End += 1
      else:
        Start += 1
        End += 1
  
  if (Text[0] == "1") and (Text[1] != "1"):
    Lonely += 1
  
  if (Text[-1] == "1") and (Text[-2] != "1"):
    Lonely += 1
  
  return Lonely

