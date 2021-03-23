"""


Create a function that inverts words or the phrase depending on the value of
parameter `type`. A **"P"** means to invert the entire phrase, while a **"W"**
means to invert every word in the phrase. See the following examples for
clarity.

### Examples

    inverter("This is Valhalla", "P") ➞ "Valhalla is this"
    
    inverter("One fine day to start", "W") ➞ "Eno enif yad ot trats"
    
    inverter("Division by powers of two", "P") ➞ "Two of powers by division"

### Notes

  * The **first character** of the returned string should be in **uppercase** and the rest are in lowercase.
  * There will be no empty strings as inputs. Punctuation marks, though quite important for grammatical correctness, are discounted in the input phrases.

"""

def inverter(Passage, Method):
  
  Blocks = Passage.split(" ")
  
  if (Method == "P"):
    
    Sentence = ""
    
    Cursor = -1
    Length = len(Blocks)
    End = Length * -1
    
    while (Cursor >= End):    
      Word = Blocks[Cursor]
      Sentence = Sentence + Word + " "
      Cursor -= 1
  
    Sentence = Sentence.rstrip(" ")
    Sentence = Sentence.capitalize()
    
    return Sentence
  
  elif (Method == "W"):
  
    Sentence = ""
    
    Counter = 0
    Length = len(Blocks)
    
    while (Counter < Length):
      Word = str(Blocks[Counter])
      Tweaked = Word[::-1]
      Sentence = Sentence + Tweaked + " "
      Counter += 1
    
    Sentence = Sentence.rstrip(" ")
    Sentence = Sentence.capitalize()
    
    return Sentence
  
  else:
    return "Something else"

