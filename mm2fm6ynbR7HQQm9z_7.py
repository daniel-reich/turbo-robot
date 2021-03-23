"""


Knights can jump across the board.

![Knights in Chess](https://edabit-challenges.s3.amazonaws.com/Rb9v.gif)

Create a function that takes a square where a knight jumps from as a `string`
and returns all the possible squares the knight can land on as a `string`.
Ignore capturing and further Chess rules. Be aware of the sides of the board.
Knights don't go over the edge, obviously.

### Examples

    knights_jump("F4") ➞ "E2,G2,D3,H3,D5,H5,E6,G6"
    
    knights_jump("A1") ➞ "C2,B3"
    
    knights_jump("E2") ➞ "C1,G1,C3,G3,D4,F4"

### Notes

  * The input is always a valid square on the board.
  * The order of the return string is A ➞ H, 1 ➞ 8.

"""

class Knight:
  rows = list('ABCDEFGH')
  
  def __init__(self, pos):
    self.pos = pos
    
    self.row = pos[0]
    self.rindex = Knight.rows.index(self.row)
    self.col = int(pos[1])
  
  def poss_moves(self):
    
    pms = []
    
    if self.rindex >= 2:
      if self.col >= 2:
        pms.append('{}{}'.format(Knight.rows[self.rindex - 2], self.col - 1))
      if self.col <= 7:
        pms.append('{}{}'.format(Knight.rows[self.rindex - 2], self.col + 1))
    
    if self.rindex >= 1:
      if self.col >= 3:
        pms.append('{}{}'.format(Knight.rows[self.rindex - 1], self.col - 2))
      if self.col <= 6:
        pms.append('{}{}'.format(Knight.rows[self.rindex - 1], self.col + 2))
    
    if self.rindex <= 5:
      if self.col >= 2:
        pms.append('{}{}'.format(Knight.rows[self.rindex + 2], self.col - 1))
      if self.col <= 7:
        pms.append('{}{}'.format(Knight.rows[self.rindex + 2], self.col + 1))
    
    if self.rindex <= 6:
      if self.col >= 3:
        pms.append('{}{}'.format(Knight.rows[self.rindex + 1], self.col - 2))
      if self.col <= 6:
        pms.append('{}{}'.format(Knight.rows[self.rindex + 1], self.col + 2))
    
    dic = {1: [pos for pos in pms if '1' in pos], 2: [pos for pos in pms if '2' in pos], 3: [pos for pos in pms if '3' in pos], 4: [pos for pos in pms if '4' in pos], 5: [pos for pos in pms if '5' in pos], 6: [pos for pos in pms if '6' in pos], 7: [pos for pos in pms if '7' in pos], 8: [pos for pos in pms if '8' in pos]}
    
    string = []
    
    for num in sorted(dic.keys()):
      if len(dic[num]) > 0:
        for l8r in Knight.rows:
          if '{}{}'.format(l8r,num) in dic[num]:
            string.append('{}{}'.format(l8r,num))
    
    return ','.join(string)
def knights_jump(square):
  
  return Knight(square).poss_moves()

