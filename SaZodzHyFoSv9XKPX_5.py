"""


 **Mubashir** was playing with dominos. He concluded that:

  * If the first domino is pushed over, it will **keep tipping next dominos to its right**.
  * Reaction will stop if a domino is **already tipped over** , or if there is an **empty space**.

![Mubashir](https://edabit-challenges.s3.amazonaws.com/329666480_orig.gif)

Create a function which takes a string of current status of the `dominos` and
returns the string after **dominos chain reaction**.

  * "|" represents a standing domino.
  * "/" represents a tripped domino.
  * " " represents an empty space.

### Examples

    domino_chain("||| ||||//| |/") ➞ "/// ||||//| |/"
    // A space will stop the reaction.
    
    domino_chain("||//||") ➞ "////||"
    // An already tripped domino will stop the reaction.
    
    domino_chain("||||") ➞ "////"

### Notes

N/A

"""

class Domino_Game:
  class Domino:
​
    def __init__(self, pos, is_dom):
​
      self.p = pos
​
      self.id = is_dom != ' '
      self.du = is_dom == '|'
​
      self.next = pos + 1
    
    def can_flip(self):
      return self.id == self.du == True
    
    def flip(self):
      self.du = False
      return True
    
    def __str__(self):
      if self.id == False:
        return ' '
      else:
        if self.du == False:
          return '/'
        else:
          return '|'
  
  def __init__(self, domino_string):
    self.ds = domino_string
​
    self.dominos = {n: Domino_Game.Domino(n, domino_string[n]) for n in range(len(domino_string))}
  
  def play(self):
    for n in sorted(self.dominos.keys()):
      domino = self.dominos[n]
      if domino.can_flip() == False:
        break
      else:
        domino.flip()
    return True
  
  def __str__(self):
    tr = ''
    for n in sorted(self.dominos.keys()):
      domino = self.dominos[n]
      tr += str(domino)
    return tr
  
​
def domino_chain(dominos):
​
  dg = Domino_Game(dominos)
​
  dg.play()
​
  return str(dg)

