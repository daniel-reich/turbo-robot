"""
Suppose a student can earn 100% on an exam by getting the answers all correct
or all incorrect. Given a **potentially incomplete** answer key and the
student's answers, write a function that determines whether or not a student
can still score 100%. Incomplete questions are marked with an underscore,
`"_"`.

    ["A", "_", "C", "_", "B"]   # answer key
    ["A", "D", "C", "E", "B"]   # student's solution
    
    ➞ True
    
    # Possible for student to get all questions correct.
    
    ["B", "_", "B"]   # answer key
    ["B", "D", "C"]   # student's solution
    
    ➞ False
    
    # First question is correct but third is wrong, so not possible to score 100%.
    
    ["T", "_", "F", "F", "F"]   # answer key
    ["F", "F", "T", "T", "T"]   # student's solution
    
    ➞ True
    
    # Possible for student to get all questions incorrect.

### Examples

    possibly_perfect(["B", "A", "_", "_"], ["B", "A", "C", "C"]) ➞ True
    
    possibly_perfect(["A", "B", "A", "_"], ["B", "A", "C", "C"]) ➞ True
    
    possibly_perfect(["A", "B", "C", "_"], ["B", "A", "C", "C"]) ➞ False
    
    possibly_perfect(["B", "_"], ["C", "A"]) ➞ True
    
    possibly_perfect(["B", "A"], ["C", "A"]) ➞ False
    
    possibly_perfect(["B"], ["B"]) ➞ True

### Notes

Test has at least one question.

"""

def possibly_perfect(key, answers):
  
  Guesses = key
  Required = answers
​
  Answered = 0
  Right = 0
  Wrong = 0
​
  Counter = 0
  Length = len(answers)
  
  while (Counter < Length):
        
    Answer = str(Guesses[Counter])
    Correct = str(Required[Counter])
    
    if (Answer == "_"):
      Counter += 1
    elif (Answer == Correct) and (Answer != "_"):
      Answered += 1
      Right += 1
      Counter += 1
    elif (Answer != Correct) and (Answer != "_"):
      Answered += 1
      Wrong += 1
      Counter += 1
    else:
      Counter += 1
  
  if (Answered == Right) or (Answered == Wrong):
    return True
  else:
    return False
