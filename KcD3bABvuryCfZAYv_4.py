"""


Write a function that returns the most frequent character in a list of words.

### Examples

    most_frequent_char(["apple", "bandage", "yodel", "make"])
    ➞ ["a", "e"]
    
    most_frequent_char(["music", "madness", "maniac", "motion"])
    ➞ ["m"]
    
    most_frequent_char(["the", "hills", "are", "alive", "with", "the", "sound", "of", "music"])
    ➞ ["e", "h", "i"]

### Notes

  * If multiple characters tie for most frequent, list all of them in alphabetical order.
  * Words will be in lower case.

"""

def most_frequent_char(lst):
  
  # Establishing Long String
  
  String = ""
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    Word = lst[Counter]
    String = String + Word
    Counter += 1
  
  Unique = []
  
  # Establishing Unique Letters
  
  Counter = 0
  Length = len(String)
  
  while (Counter < Length):
    
    Letter = String[Counter]
    
    if (Letter in Unique):
      Counter += 1
    else:
      Unique.append(Letter)
      Counter += 1
  
  # Establishing Occurrences of Unique Letters
  
  Maximum = 0
  
  Counter = 0
  Length = len(Unique)
  
  while (Counter < Length):
    Letter = Unique[Counter]
    Events = String.count(Letter)
    
    if (Events > Maximum):
      Maximum = Events
      Counter += 1
    else:
      Counter += 1
  
  # Establishing Letters of Highest Count
  
  Wanted = []
  
  Counter = 0
  Length = len(String)
  
  while (Counter < Length):
    Letter = String[Counter]
    Events = String.count(Letter)
    
    if (Events == Maximum) and (Letter not in Wanted):
      Wanted.append(Letter)
      Counter += 1
    else:
      Counter += 1
  
  Wanted = sorted(Wanted)
  
  return Wanted

