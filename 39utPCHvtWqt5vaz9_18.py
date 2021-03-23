"""


You will be given a list of string `"east"` formatted differently every time.
Create a function that returns `"west"` wherever there is `"east"`. Format the
string according to the input. Check the examples below to better understand
the question.

### Examples

    direction(["east", "EAST", "eastEAST"]) ➞ ["west", "WEST", "westWEST"]
    
    direction(["eAsT EaSt", "EaSt eAsT"]) ➞ ["wEsT WeSt", "WeSt wEsT"]
    
    direction(["east EAST", "e a s t", "E A S T"]) ➞ ["west WEST", "w e s t", "W E S T"]

### Notes

The input will only be `"east"` in different formats.

"""

def direction(lst):
  
  Revised = []
    
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
      
    Sample = lst[Counter]
    Tweaked = ""
    
    Previous = "X"
    
    Cursor = 0
    Span = len(Sample)
    
    while (Cursor < Span):
      
      Item = Sample[Cursor]
      
      if (Previous == "X") and (Item == "E"):
        Tweaked = Tweaked + "W"
        Previous = "E"
        Cursor += 1
      elif (Previous == "X") and (Item == "e"):
        Tweaked = Tweaked + "w"
        Previous = "E"
        Cursor += 1
      
      elif (Previous == "E") and (Item == "a"):
        Tweaked = Tweaked + "e"
        Previous = "A"
        Cursor += 1
      elif (Previous == "E") and (Item == "A"):
        Tweaked = Tweaked + "E"
        Previous = "A"
        Cursor += 1
      
      elif (Previous == "A") and (Item == "s"):
        Tweaked = Tweaked + "s"
        Previous = "S"
        Cursor += 1
      elif (Previous == "A") and (Item == "S"):
        Tweaked = Tweaked + "S"
        Previous = "S"
        Cursor += 1
      
      elif (Previous == "S") and (Item == "t"):
        Tweaked = Tweaked + "t"
        Previous = "X"
        Cursor += 1
      elif (Previous == "S") and (Item == "T"):
        Tweaked = Tweaked + "T"
        Previous = "X"
        Cursor += 1
    
      elif (Item == " "):
        Tweaked = Tweaked + Item
        Cursor += 1
      
      else:
        return "Error!"
      
    Revised.append(Tweaked)
    Counter +=1
  
  return Revised

