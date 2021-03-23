"""


Given a sentence, return the number of words which have the **same first and
last letter**.

### Examples

    count_same_ends("Pop! goes the balloon") ➞ 1
    
    count_same_ends("And the crowd goes wild!") ➞ 0
    
    count_same_ends("No I am not in a gang.") ➞ 1

### Notes

  * Don't count single character words (such as "I" and "A" in example #3).
  * The function should not be case sensitive, meaning a capital "P" should match with a lowercase one.
  * Mind the punctuation!
  * Bonus points indeed for using regex!

"""

def count_same_ends(txt):
  
  # Removing Punctuation
  
  Allowed = " abcdefghijklmnopqrstuvwxyz"
  Revision_One = ""
  
  Counter = 0
  Length = len(txt)
  
  while (Counter < Length):
    
    Item = txt[Counter].lower()
    
    if (Item in Allowed):
      Revision_One = Revision_One + Item.lower()
      Counter += 1
    else:
      Counter += 1
  
  # Splitting into Word Blocks
  Blocks = Revision_One.split(" ")
  
  # Bucket for Answer
  Answer = 0
  
  # Checking Ends of Words
  Counter = 0
  Length = len(Blocks)
  
  while (Counter < Length):
    Item = Blocks[Counter]
    Span = len(Item)
    First = Item[0]
    Last = Item[-1]
    
    if (First == Last) and (Span > 1):
      Answer += 1
      Counter += 1
    else:
      Counter += 1
  
  # Giving Answer
  return Answer

