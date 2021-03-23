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
  out_lst = []
  for item in lst:
    word = ""
    for letter in item:
      if letter == ' ':
        word += ' '
      if letter.lower() == 'e':
        word += 'W' if letter == letter.upper() else 'w'
      if letter.lower() == 'a':
        word += 'E' if letter == letter.upper() else 'e'
      if letter.lower() == 's':
        word += 'S' if letter == letter.upper() else 's'
      if letter.lower() == 't':
        word += 'T' if letter == letter.upper() else 't'
    out_lst.append(word)
  return out_lst

