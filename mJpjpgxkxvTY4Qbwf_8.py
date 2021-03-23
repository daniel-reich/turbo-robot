"""


Create a function that takes a 5x5 3D list and returns `True` if it has at
least one Bingo, and `False` if it doesn't.

### Examples

    bingo_check([
      [45, "x", 31, 74, 87],
      [64, "x", 47, 32, 90],
      [37, "x", 68, 83, 54],
      [67, "x", 98, 39, 44],
      [21, "x", 24, 30, 52]
    ]) ➞ True
    
    bingo_check([
      ["x", 43, 31, 74, 87],
      [64, "x", 47, 32, 90],
      [37, 65, "x", 83, 54],
      [67, 98, 39, "x", 44],
      [21, 59, 24, 30, "x"]
    ]) ➞ True
    
    bingo_check([
      ["x", "x", "x", "x", "x"],
      [64, 12, 47, 32, 90],
      [37, 16, 68, 83, 54],
      [67, 19, 98, 39, 44],
      [21, 75, 24, 30, 52]
    ]) ➞ True
    
    bingo_check([
      [45, "x", 31, 74, 87],
      [64, 78, 47, "x", 90],
      [37, "x", 68, 83, 54],
      [67, "x", 98, "x", 44],
      [21, "x", 24, 30, 52]
    ]) ➞ False

### Notes

Only check for diagnols, horizontals and verticals.

"""

def bingo_check(board):
  l=board
  def check_horz(l):
    for i in range(len(l)):
          if (len(set(l[i])))==1:
             return True
             break
    else:
        return False
  def check_colm(l):
    for i in range(len(l)):
      c=[]
      for j in range(len(l)):
        c.append(l[j][i])
      if (len(set(c)))==1:
             return True
             break
    else:
        return False        
  def check_diag1(l):
    c=[]
    for i in range(len(l)):
      for j in range(len(l)):
        if i==j:
          c.append(l[i][j])
    if (len(set(c)))==1:
             return True
    else:
        return False 
  def check_diag2(l):
    c=[]
    for i in range(len(l)):
      for j in range(len(l)):
        if i==j:
          c.append(l[i][4-i])
    if (len(set(c)))==1:
             return True
    else:
        return False 
  return  check_horz(l) or check_colm(l) or check_diag2(l) or check_diag1(l)

