"""


Write a function that will return the **longest word** in a sentence. In cases
where more than one word is found, return the first one.

### Examples

    find_longest("A thing of beauty is a joy forever.") ➞ "forever"
    
    find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"
    
    find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"

### Notes

  * Special characters and symbols _don't count_ as part of the word.
  * Return the longest word found in **lowercase** letters.
  * A recursive version of this challenge can be found in [here](https://edabit.com/challenge/LyzKTyYdKF4oDf5bG).

"""

def find_longest(sentence):
  
  # Converting Sentence to Lower Case
  Sample = sentence.lower()
  
  # Establishing 'Allowed' Letters
  # (to filter out punctuation)
  Allowed = " abcedefghijklmnopqrstuvwxyz"
  
  # Bucket for Punctuation Free Sentence
  Revised = ""
  
  # Extracting Non-Punctuation Items
  Counter = 0
  Length = len(Sample)
  
  while (Counter < Length):
    Item = Sample[Counter]
    
    if (Item in Allowed):
      Revised = Revised + Item
      Counter += 1
    else:
      Revised = Revised + " "
      Counter += 1
  
  # Splitting Revised into Word Blocks
  Blocks = Revised.split(" ")
  
  # Buckets for Answer
  Answer = ""
  Target = 0
  
  # Establishing Longest Word
  Counter = 0
  Length = len(Blocks)
  
  while (Counter < Length):
    Item = Blocks[Counter]
    Span = len(Item)
    
    if (Span > Target):
      Answer = Item
      Target = Span
      Counter += 1
    else:
      Counter += 1
  
  # Giving Answer
  return Answer

