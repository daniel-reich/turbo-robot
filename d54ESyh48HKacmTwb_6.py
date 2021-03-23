"""


Create a function that takes a list of numbers and returns the _greatest
common factor_ of those numbers.

### Examples

    gcd([84, 70, 42, 56]) ➞ 14
    
    gcd([19, 38, 76, 133]) ➞ 19
    
    gcd([120, 300, 95, 425, 625]) ➞ 5

### Notes

The GCD is the largest factor that divides all numbers in the list.

"""

def gcd(lst):
  
  Floor = min(lst)
  Answer = 1
  Candidate = 2
  
  while (Candidate <= Floor):
  
    Divisible = 0
    Counter = 0
    Length = len(lst)
    
    while (Counter < Length):
      
      Item = lst[Counter]
      
      if (Item % Candidate == 0):
        Divisible += 1
        Counter += 1
      else:
        Counter += 1
    
    if (Divisible == Length):
      Answer = Candidate
      Candidate += 1
    else:
      Candidate += 1
  
  return Answer

