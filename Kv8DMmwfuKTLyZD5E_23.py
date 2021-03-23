"""


Create a function which creates a square dartboard of side length `n`. The
value of a number should increase, the closer it is to the centre of the
board.

### Examples

    make_dartboard(3) ➞ [
      111,
      121,
      111
    ]
    
    make_dartboard(8) ➞ [
      11111111,
      12222221,
      12333321,
      12344321,
      12344321,
      12333321,
      12222221,
      11111111
    ]
    
    make_dartboard(5) ➞ [
      11111,
      12221,
      12321,
      12221,
      11111
    ]

### Notes

If the size given is an even number, the centre should be made up of the 4
highest values.

"""

def make_dartboard(n):
  
  if (n % 2 == 0):
    Ceiling = n/2
  else:
    Ceiling = (n+1) / 2
  
  Front = ""
  Back = ""
  Inside_Number = 1
  
  Top_Half = []
  Bottom_Half = []
  
  Layers = 0
  
  while (Layers < Ceiling):
    
    Row = ""
    
    if (Front == ""):
      FL = 0
    else:
      FL = len(Front)
    
    if (Back == ""):
      BL = 0
    else:
      BL = len(Back)
    
    Middle = ""
    Added = 0
    Required = n - FL - BL  
    
    while (Added < Required):
      Middle = Middle + str(Inside_Number)
      Added += 1
    
    Row = Front + Middle + Back
    Row = int(Row)
    
    Top_Half.append(Row)
    Bottom_Half.insert(0,Row)
    
    Front = Front + str(Inside_Number)
    Back = str(Inside_Number) + Back
    
    Inside_Number += 1
    Layers += 1
  
  if (n % 2 == 0):
    Dartboard = Top_Half + Bottom_Half
    return Dartboard
  else:
    Dartboard = Top_Half + Bottom_Half[1:]
    return Dartboard

