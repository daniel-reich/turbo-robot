"""


Create a function that expands a decimal number into a string as shown below:

    25.24 ➞ "20 + 5 + 2/10 + 4/100"
    70701.05 ➞ "70000 + 700 + 1 + 5/100"
    685.27 ➞ "600 + 80 + 5 + 2/10 + 7/100"

### Examples

    expanded_form(87.04) ➞ "80 + 7 + 4/100"
    
    expanded_form(123.025) ➞ "100 + 20 + 3 + 2/100 + 5/1000"
    
    expanded_form(50.270) ➞ "50 + 2/10 + 7/100"

### Notes

N/A

"""

def expanded_form(num):
  
  #   Converting 'num' to Text
  Text = str(num)
  Blocks = Text.split(".")
  
  Whole = Blocks[0]
  Part = Blocks[1]
  
  #   Buckets for Passages of Text
  Pieces = []
  
  #   Going Through Whole Number Section
  Cursor = len(Whole) - 1
  Multiple = 1
  
  while (Cursor >= 0):
    
    Item = Whole[Cursor]
    
    if (Item == "0"):
      Multiple *= 10
      Cursor -= 1
    else:
      Score = int(Item) * Multiple
      Passage = str(Score)
      Pieces.insert(0, Passage)
      Multiple *= 10
      Cursor -= 1
  
  #   Going Through Part Number Section
  Multiple = 10
  
  Cursor = 0
  Length = len(Part)
  
  while (Cursor < Length):
    
    Item = Part[Cursor]
    
    if (Item == "0"):
      Multiple *= 10
      Cursor += 1
    else:
      Passage = Item + "/" + str(Multiple)
      Pieces.append(Passage)
      Multiple *= 10
      Cursor += 1
  
  #   Building and Giving Answer
  Link = " + "
  Answer = Link.join(Pieces)
  return Answer

