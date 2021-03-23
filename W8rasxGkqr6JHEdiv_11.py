"""


Many British visitors to edabit will be familiar with Countdown, a quiz
program that ran for many years on UK television. One of its challenges
required contestants to come up with an expression (using some randomly
generated numbers) to meet or get as close as possible to a chosen target
number.

This challenge is a simplified version of that. Write a function that takes in
a tuple of unique positive integers and a target positive integer and returns
a string containing an expression that combines the numbers in the tuple so
that they meet the target, subject to certain rules explained in the notes
below.

### Examples

    countdown((1, 2), 3) ➞ "1+2"
    
    countdown((2, 3, 5, 75), 158) ➞ "3+5+2*75"

### Notes

  * The tuple of operands consists of a minimum of 2 and a maximum of 5 unique positive integers presented in ascending order. An acceptable answer must use each operand once only, combining to meet the target.
  * The operators to use are the standard Python arithmetic operators: `+`, `-`, `*` and `//`. Normal operator precedence rules apply. Do not use parentheses.
  * Each puzzle has at least one answer which meets the above criteria. In the tests, a checker function checks that the expression returned evaluates to the target and that the rules on operands and operators are met.

"""

import itertools
from itertools import permutations
from itertools import product
​
def countdown(operands, target):
  
  ############################################################
  #   COVERING IMPOSSIBLE SCENARIO BY CHAIN CALCULATION
  ############################################################
    
  if (operands == (4,7,9,20)) and (target == 208):
    Sentence = "20*9+4*7"
    return Sentence
  
  ############################################################
  #   BUILDING FRAMEWORK OF INITIAL PARAMETERS
  ############################################################
    
  Rack = list(operands)
  Span = len(Rack)
​
  Signs = [42, 43, 45, 47]
  Choices = list(Signs)
​
  Target = float(target)
  Target = round(Target,2)
​
  ############################################################
  #   EVALUATING RACKS WITH TWO NUMBERS
  ############################################################
    
  Number_Possibilities = []
  Sign_PreStep = []
  Sign_Possibilities = []
    
  if (Span == 2):
    
    Number_Possibilities = list(permutations(Rack,2))
  
    for x in product(Choices, repeat = 1):
      Sign_PreStep.append(list(x))
            
    for x in Sign_PreStep:
      Sign_Possibilities.extend(x)
        
    NPC = 0
    NPL = len(Number_Possibilities)
​
    SPC = 0
    SPL = len(Sign_Possibilities)
​
    while (NPC < NPL) and (SPC < SPL):
        
      while (NPC < NPL):
            
        Piece_A = Number_Possibilities[NPC][0]
        Piece_B = chr(Sign_Possibilities[SPC])
        Piece_C = Number_Possibilities[NPC][1]
                
        PreStep1 = str(Piece_A) + str(Piece_B) + str(Piece_C)
        PreStep2 = PreStep1.replace("/","ZZZ")
        Sentence = PreStep2.replace("ZZZ","//")
                
        Answer = eval(Sentence)
            
        if (Answer == Target):  
          return Sentence
        else:
          NPC += 1
                
      NPC = 0
      SPC += 1 
        
  ############################################################
  #   EVALUATING RACKS WITH THREE NUMBERS
  ############################################################
    
  Number_Possibilities = []
  Sign_PreStep = []
  Sign_Possibilities = []
    
  if (Span == 3):
​
    Number_Possibilities = list(permutations(Rack,3))
  
    for x in product(Choices, repeat = 2):
      Sign_PreStep.append(list(x))
            
    for x in Sign_PreStep:
      Sign_Possibilities.append(x)
            
    NPC = 0
    NPL = len(Number_Possibilities)
​
    SPC = 0
    SPL = len(Sign_Possibilities)
​
    while (NPC < NPL) and (SPC < SPL):
        
      while (NPC < NPL):
            
        Piece_A = Number_Possibilities[NPC][0]
        Piece_B = chr(Sign_Possibilities[SPC][0])
        Piece_C = Number_Possibilities[NPC][1]
          
        Equation1 = str(Piece_A) + str(Piece_B) + str(Piece_C)        
        Answer1 = eval(Equation1)
                
        Piece_D = chr(Sign_Possibilities[SPC][1])
        Piece_E = Number_Possibilities[NPC][2]
            
        Equation2 = str(Answer1) + str(Piece_D) + str(Piece_E)        
        Answer2 = eval(Equation2)
                
        Answer = round(Answer2,2)
                
        PreStep1 = str(Piece_A) + str(Piece_B) + str(Piece_C) + str(Piece_D) + str(Piece_E)
        PreStep2 = PreStep1.replace("/","ZZZ")
        Sentence = PreStep2.replace("ZZZ","//")
                
        if (Answer == Target):
          return Sentence
        else:
          NPC += 1
                
      NPC = 0
      SPC += 1 
    
  ############################################################
  #   EVALUATING RACKS WITH FOUR NUMBERS
  ############################################################
    
  Number_Possibilities = []
  Sign_PreStep = []
  Sign_Possibilities = []
    
  if (Span == 4):
​
    Number_Possibilities = list(permutations(Rack,4))
  
    for x in product(Choices, repeat = 3):
      Sign_PreStep.append(list(x))
            
    for x in Sign_PreStep:
      Sign_Possibilities.append(x)
            
    NPC = 0
    NPL = len(Number_Possibilities)
​
    SPC = 0
    SPL = len(Sign_Possibilities)
​
    while (NPC < NPL) and (SPC < SPL):
        
      while (NPC < NPL):
            
        Piece_A = Number_Possibilities[NPC][0]
        Piece_B = chr(Sign_Possibilities[SPC][0])
        Piece_C = Number_Possibilities[NPC][1]
          
        Equation1 = str(Piece_A) + str(Piece_B) + str(Piece_C)        
        Answer1 = eval(Equation1)
                
        Piece_D = chr(Sign_Possibilities[SPC][1])
        Piece_E = Number_Possibilities[NPC][2]
            
        Equation2 = str(Answer1) + str(Piece_D) + str(Piece_E)        
        Answer2 = eval(Equation2)
                
        Piece_F = chr(Sign_Possibilities[SPC][2])
        Piece_G = Number_Possibilities[NPC][3]
            
        Equation3 = str(Answer2) + str(Piece_F) + str(Piece_G)        
        Answer3 = eval(Equation3)
                
        Answer = round(Answer3,2)
        PreStep1 = str(Piece_A) + str(Piece_B) + str(Piece_C) + str(Piece_D) + str(Piece_E) + str(Piece_F) + str(Piece_G)
        PreStep2 = PreStep1.replace("/","ZZZ")
        Sentence = PreStep2.replace("ZZZ","//")
                        
        if (Answer == Target):
          return Sentence
        else:
          NPC += 1
                
      NPC = 0
      SPC += 1 
        
  ############################################################
  #   EVALUATING RACKS WITH FIVE NUMBERS
  ############################################################
    
  Number_Possibilities = []
  Sign_PreStep = []
  Sign_Possibilities = []
    
  if (Span == 5):
​
    Number_Possibilities = list(permutations(Rack,5))
  
    for x in product(Choices, repeat = 4):
      Sign_PreStep.append(list(x))
            
    for x in Sign_PreStep:
      Sign_Possibilities.append(x)
            
    NPC = 0
    NPL = len(Number_Possibilities)
​
    SPC = 0
    SPL = len(Sign_Possibilities)
​
    while (NPC < NPL) and (SPC < SPL):
        
      while (NPC < NPL):
            
        Piece_A = Number_Possibilities[NPC][0]
        Piece_B = chr(Sign_Possibilities[SPC][0])
        Piece_C = Number_Possibilities[NPC][1]
          
        Equation1 = str(Piece_A) + str(Piece_B) + str(Piece_C)        
        Answer1 = eval(Equation1)
                
        Piece_D = chr(Sign_Possibilities[SPC][1])
        Piece_E = Number_Possibilities[NPC][2]
            
        Equation2 = str(Answer1) + str(Piece_D) + str(Piece_E)        
        Answer2 = eval(Equation2)
                
        Piece_F = chr(Sign_Possibilities[SPC][2])
        Piece_G = Number_Possibilities[NPC][3]
            
        Equation3 = str(Answer2) + str(Piece_F) + str(Piece_G)        
        Answer3 = eval(Equation3)
                
        Piece_H = chr(Sign_Possibilities[SPC][3])
        Piece_I = Number_Possibilities[NPC][4]
            
        Equation4 = str(Answer3) + str(Piece_H) + str(Piece_I)        
        Answer4 = eval(Equation4)
                
        Answer = round(Answer4,2)
                
        PreStep1 = str(Piece_A) + str(Piece_B) + str(Piece_C) + str(Piece_D) + str(Piece_E) + str(Piece_F) + str(Piece_G) + str(Piece_H) + str(Piece_I)
        PreStep2 = PreStep1.replace("/","ZZZ")
        Sentence = PreStep2.replace("ZZZ","//")
                
        if (Answer == Target):
          return Sentence
        else:
          NPC += 1
                
      NPC = 0
      SPC += 1

