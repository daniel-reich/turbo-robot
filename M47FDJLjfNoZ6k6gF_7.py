"""


There are three cups on a table, at positions **A, B, and C.** At the start,
there is a ball hidden under the cup at **position B**.

![Image of cups where ball is under middle cup](https://edabit-
challenges.s3.amazonaws.com/kfnerNJDNn.png)

However, I perform several swaps on the cups, which is notated as two letters.
For example, if I swap the cups at positions **A and B** , I could notate this
as `AB` or `BA`.

Create a function that returns the letter position that the ball is at, once I
finish swapping the cups. The swaps will be given to you as a list.

### Worked Example

    cup_swapping(["AB", "CA", "AB"]) ➞ "C"
    
    # Ball begins at position B.
    # Cups A and B swap, so the ball is at position A.
    # Cups C and A swap, so the ball is at position C.
    # Cups A and B swap, but the ball is at position C, so it doesn't move.

### Examples

    cup_swapping(["AB", "CA"]) ➞ "C"
    
    cup_swapping(["AC", "CA", "CA", "AC"]) ➞ "B"
    
    cup_swapping(["BA", "AC", "CA", "BC"]) ➞ "A"

### Notes

  * A swap could be notated in two different ways, since both ways end up with the same outcome.
  * All swaps will be notated as capital letters and will be valid.
  * You cannot swap a cup with itself.

"""

class Board:
  class Cup:
​
    def __init__(self, ident, ball = False):
      self.id = ident
      self.ball = ball
    
    def switch(self, other):
      if self.ball == False and other.ball == False:
        return False
      elif other.ball == True:
        self.ball = True
        other.ball = False
        return True
      else:
        self.ball = False
        other.ball = True
        return True
  
  def __init__(self, ball_start_pos):
​
    if ball_start_pos == 'A':
      self.a = Board.Cup('A', True)
    else:
      self.a = Board.Cup('A')
    
    if ball_start_pos == 'B':
      self.b = Board.Cup('B', True)
    else:
      self.b = Board.Cup('B')
    
    if ball_start_pos == 'C':
      self.c = Board.Cup('C', True)
    else:
      self.c = Board.Cup('C')
    
    self.cups = {'A': self.a, 'B': self.b, 'C': self.c}
  
  def interpret(self, string):
​
    c1 = self.cups[string[0]]
    c2 = self.cups[string[1]]
​
    return c1.switch(c2)
  
  def find_ball(self):
    for cup in self.cups.values():
      if cup.ball == True:
        return cup.id
    return False
​
​
def cup_swapping(swaps):
​
  board = Board('B')
​
  for swap in swaps:
    board.interpret(swap)
  
  return board.find_ball()

