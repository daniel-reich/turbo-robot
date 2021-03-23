"""


Given two integers as arguments, create a function that finds the largest
prime within the range of the two integers.

### Examples

    fat_prime(2, 10) ➞ 7
    # range [2, 3, 4, 5, 6, 7, 8, 9, 10] and the largest prime is 7.
    
    fat_prime(10, 2) ➞ 7
    # [10, 9, 8, 7, 6, 5, 4, 3, 2] and the largest prime is 7.
    
    fat_prime(4, 24) ➞ 23
    # range [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] the largest prime is 23.

### Notes

All numbers will be positive integers.

"""

############################################################
#   Sub Function
############################################################
​
def FNC_Prime_Number_Checker(Number):
​
  Factors = []
  Tester = 1
  
  while (Tester <= Number):
    
    if (Number % Tester == 0):
      Factors.append(Tester)
      Tester += 1
    else:
      Tester += 1
  
  Span = len(Factors)
  
  if (Span == 2):
    return True
  else:
    return False
​
############################################################
#   MAIN FUNCTION
############################################################
​
def fat_prime(a, b):
  
  Answer = max(a,b)
  
  while (Answer >= min(a,b)):
  
    if FNC_Prime_Number_Checker(Answer):
      return Answer
    else:
      Answer -= 1
      
  return "No Prime Number in Range"

