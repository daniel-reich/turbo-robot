"""


A string is an **almost-palindrome** if, by changing **only one character** ,
you can make it a palindrome. Create a function that returns `True` if a
string is an **almost-palindrome** and `False` otherwise.

### Examples

    almost_palindrome("abcdcbg") ➞ True
    # Transformed to "abcdcba" by changing "g" to "a".
    
    almost_palindrome("abccia") ➞ True
    # Transformed to "abccba" by changing "i" to "b".
    
    almost_palindrome("abcdaaa") ➞ False
    # Can't be transformed to a palindrome in exactly 1 turn.
    
    almost_palindrome("1234312") ➞ False

### Notes

Return `False` if the string is already a palindrome.

"""

def almost_palindrome(txt):
  
  # Establishing Palindrome Samples for Comparison
  
  Sample = str(txt)
  Length = len(Sample)
  
  if (Length % 2 == 0):
    Halfway = int(Length / 2)
    Left = Sample[0:Halfway]
    Right = Sample[Halfway:]
    
    Exhibit_A = Left + Left[::-1]
    Exhibit_B = Right + Right[::-1]
  
  else:
    
    PreStep_A1 = Length - 1
    PreStep_A2 = int(PreStep_A1 / 2)
    A = PreStep_A2
    Left_1 = Sample[0:A]
    Left_2 = Left_1[::-1]
    
    B = A
    Middle = Sample[B]
    
    C = A + 1
    Right_2 = Sample[C:]
    Right_1 = Right_2[::-1]
    
    Exhibit_A = Left_1 + Middle + Left_2
    Exhibit_B = Right_1 + Middle + Right_2
  
  # Establishing Comparison to Exhibit_A
  
  Sample = str(txt)
  Changes = 0
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    Item_A = Exhibit_A[Counter]
    Item_B = Sample[Counter]
    
    if (Item_A == Item_B):
      Counter += 1
    else:
      Changes += 1
      Counter += 1
  
  if (Changes == 1):
    return True
  
  # Establishing Comparison to Exhibit_B
  
  Sample = str(txt)
  Changes = 0
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    Item_A = Sample[Counter]
    Item_B = Exhibit_B[Counter]
    
    if (Item_A == Item_B):
      Counter += 1
    else:
      Changes += 1
      Counter += 1
  
  if (Changes == 1):
    return True
  else:
    return False

