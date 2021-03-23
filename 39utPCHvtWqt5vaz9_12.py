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
  replacements = {'e':'w','a':'e','E':'W','A':'E'}
  out = []
  for item in lst:  
    word = "".join([replacements.get(c, c) for c in item])
    out.append(word)
  return out

