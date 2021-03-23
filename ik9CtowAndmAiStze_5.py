"""


The function is given a string. Sort the characters and return a new string.
Sorting conditions:

  * Most frequent move in front.
  * For the same frequency upper case characters move in front.
  * For the same frequency and case sort them alphabetically.

### Examples

    frequency_sort("tree") ➞ "eert"
    
    frequency_sort("cccaaa") ➞ "aaaccc"
    
    frequency_sort("Aabb") ➞ "bbAa"

### Notes

N/A

"""

def frequency_sort(s):
  
  #   Establishing Unique Letters of 's'
  Featured = []
  
  Counter = 0
  Length = len(s)
  
  while (Counter < Length):
    
    Item = s[Counter]
    
    if (Item not in Featured):
      Featured.append(Item)
      Counter += 1
    else:
      Counter += 1
  
  #   Building Blocks of Repeated Letters for Each Unique Character
  Blocks = []
  Featured = sorted(Featured)
  Highest = 0
  
  Counter = 0
  Length = len(Featured)
  
  while (Counter < Length):
    
    Batch = ""
    Item = Featured[Counter]
    
    Added = 0
    Required = s.count(Item)
    
    while (Added < Required):
      Batch = Batch + Item
      Added += 1
    
    Blocks.append(Batch)
    
    if (Required > Highest):
      Highest = Required
      Counter += 1
    else:
      Counter += 1
      
  #   Bucket for Answer
  Answer = ""
  
  #   Building Answer
  Seeking = Highest
  
  while (Seeking > 0):
    
    Counter = 0
    Length = len(Blocks)
    
    while (Counter < Length):
      
      Batch = Blocks[Counter]
      Span = len(Batch)
      
      if (Span == Seeking):
        Answer = Answer + Batch
        Counter += 1
      else:
        Counter += 1
        
    Seeking -= 1
    
  #   Giving Answer
  return Answer

