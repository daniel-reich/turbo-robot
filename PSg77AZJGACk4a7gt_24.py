"""


For this challenge, forget how to add two numbers together. The best
explanation on what to do for this function is this meme:

![Alternative Text](https://edabit-challenges.s3.amazonaws.com/caf.jpg)

### Examples

    meme_sum(26, 39) ➞ 515
    # 2+3 = 5, 6+9 = 15
    # 26 + 39 = 515
    
    meme_sum(122, 81) ➞ 1103
    # 1+0 = 1, 2+8 = 10, 2+1 = 3
    # 122 + 81 = 1103
    
    meme_sum(1222, 30277) ➞ 31499

### Notes

N/A

"""

def meme_sum(a, b):
  
  # Converting Parameters to String
  
  Text_A = str(a)
  Length_A = len(Text_A)
  
  Text_B = str(b)
  Length_B = len(Text_B)
  
  # Making Sure Both Strings Are Same Length
  
  while (Length_A < Length_B):
    Text_A = "0" + Text_A
    Length_A = len(Text_A)
    Length_B = len(Text_B)
    
  while (Length_B < Length_A):
    Text_B = "0" + Text_B
    Length_A = len(Text_A)
    Length_B = len(Text_B)
    
  # Bucket for Answer
  Answer = ""
  
  # Performing 'Mathematics'
  
  Counter = 0
  Length = len(Text_A)
  
  while (Counter < Length):
    
    Item_A = Text_A[Counter]
    Digit_A = int(Item_A)
    
    Item_B = Text_B[Counter]
    Digit_B = int(Item_B)
    
    Score = Digit_A + Digit_B
    Passage = str(Score)
    
    Answer = Answer + Passage
    Counter += 1
    
  # Converting Answer to Integer and Giving Answer
  Answer = int(Answer)
  return Answer

