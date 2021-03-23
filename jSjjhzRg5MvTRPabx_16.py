"""


Given a list of strings (nouns), list them up in a complete sentence.

### Examples

    sentence(["orange", "apple", "pear"]) ➞ "An orange, an apple and a pear."
    
    sentence(["keyboard", "mouse"]) ➞ "A keyboard and a mouse."
    
    sentence(["car", "plane", "truck", "boat"]) ➞ "A car, a plane, a truck and a boat."

### Notes

  * The sentence starts with a **capital letter**.
  * Do not change **the order** of the words.
  *  **A/An** should be correct in all places.
  * Put commas between nouns, except between the last two (there you put "and").
  * The sentence ends with a `.`
  * There are at least two nouns given.
  * Every given word is lowercase.

"""

def sentence(Sample):
  
  Sentence = ""
  Vowels = "aeiuo"
  
  Counter = 0
  Length = len(Sample)
  Last = Length - 1
  
  while (Counter < Length):
    
    Word = Sample[Counter]
    Initial = Word[0]
    
    if (Counter == 0) and (Initial in Vowels):
      Sentence = Sentence + "An " + Word
      Counter += 1
    elif (Counter == 0) and (Initial not in Vowels):
      Sentence = Sentence + "A " + Word
      Counter += 1
    
    elif (Counter == Last) and (Initial in Vowels):
      Sentence = Sentence + " and an " + Word + "."
      Counter += 1
    elif (Counter == Last) and (Initial not in Vowels):
      Sentence = Sentence + " and a " + Word + "."
      Counter += 1
    
    elif (Initial in Vowels):
      Sentence = Sentence + ", an " + Word
      Counter += 1
    elif (Initial not in Vowels):
      Sentence = Sentence + ", a " + Word
      Counter += 1
      
    else:
      Counter += 1
​
  return Sentence

