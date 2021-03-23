"""


Given two strings, that may or may not be of the same length, determine the
minimum number of character deletions required to make an anagram. Any
characters can be deleted from either of the strings.

### Examples

    make_anagram("cde", "abc") ➞ 4
    # Remove d and e from cde to get c.
    # Remove a and b from abc to get c.
    # It takes 4 deletions to make both strings anagrams.
    
    make_anagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke") ➞ 30
    
    make_anagram("showman", "woman") ➞ 2

### Notes

N/A

"""

def make_anagram(a, b):
  
  Combined = a + b
  
  Chunks = []
  
  Counter = 0
  Length = len(Combined)
  
  while (Counter < Length):
    
    Item = Combined[Counter]
    
    if (Item in Chunks):
      Counter += 1
    else:
      Chunks.append(Item)
      Counter += 1
  
  Total = 0
  
  Counter = 0
  Length = len(Chunks)
  
  while (Counter < Length):
    
    Item = Chunks[Counter]
    
    Score_A = a.count(Item)
    Score_B = b.count(Item)
    
    Removals = abs(Score_A - Score_B)
    Total += Removals
    
    Counter += 1
    
  return Total

