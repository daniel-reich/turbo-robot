"""


Create a function that takes in a sentence and returns the average length of
each word in that sentence. Round your result to two decimal places.

### Examples

    average_word_length("A B C.") ➞ 1.00
    
    average_word_length("What a gorgeous day.") ➞ 4.00
    
    average_word_length("Dude, this is so awesome!") ➞ 3.80

### Notes

Ignore punctuation when counting the length of a word.

"""

def average_word_length(txt):
  
  Sample = str(txt)
  
  Blocks = Sample.split(" ")
  Words = len(Blocks)
  
  Letters = 0
  
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    Item = Sample[Counter]
    
    if (Item.isalpha()):
      Letters += 1
      Counter += 1
    else:
      Counter += 1
  
  Answer = round(Letters/Words, 2)
  
  return Answer

