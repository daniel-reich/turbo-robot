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
  sl = lambda l: 'w'*(l == 'e') + 'e'*(l == 'a') if l not in 'st' else l  #switch letter
  kc = lambda x, y: x.upper()*(y.isupper()) + x.lower()*(y.islower())  # keep case
  directions = []
  for _ in lst:
    new_dir = ''
    for letter in _: new_dir += kc(sl(letter.lower()), letter) if letter != ' ' else ' '
    directions.append(new_dir)
  return directions

