"""


You're head of security at a casino that has money being stolen from it. You
get the data in the form of strings and you have to set off an alarm if a
thief is detected.

  * If there is no guard between thief and money, return `"ALARM!"`
  * If the money is protected, return `"Safe"`

### String Components

  * x - Empty Space
  * T - Thief
  * G - Guard
  * $ - Money

### Examples

    security("xxxxTTxGxx$xxTxxx") ➞ "ALARM!"
    
    security("xxTxxG$xxxx$xxxx") ➞ "Safe"
    
    security("TTxxxx$xxGxx$Gxxx") ➞ "ALARM!"

### Notes

Money at the extremes are safe.

"""

class Map:
​
  class Space:
​
    def __init__(self, pos, tpe):
      self.pos = pos
      self.type = tpe
​
    def find_path_to(self, other):
      poss = [pos for pos in range(min(self.pos,other.pos), max(self.pos,other.pos) + 1)]
      return poss
  
  def __init__(self, string):
    self.raw = string
​
    self.spaces = {}
    self.theives = []
    self.guards = []
    self.money = []
​
    for n in range(len(self.raw)):
      space = Map.Space(n, string[n])
      self.spaces[n] = space
      if space.type == 'T':
        self.theives.append(n)
      if space.type == 'G':
        self.guards.append(n)
      if space.type == '$':
        self.money.append(n)
  
  def is_safe(self):
​
    for theif in self.theives:
      theif = self.spaces[theif]
      for pay in self.money:
        path = theif.find_path_to(self.spaces[pay])
        blocked = False
        for guard in self.guards:
          if guard in path:
            blocked = True
            break
        if blocked == False:
          return False
    
    return True
  
def security(txt):
​
  bank = Map(txt)
​
  return 'Safe' if bank.is_safe() == True else 'Alarm!'.upper()

