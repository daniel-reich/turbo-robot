"""


Your chess teacher wants to know if a bishop can reach a certain spot on the
board in the given amount of moves.

Given a starting square `start`, ending square `end` and the maximum number of
moves allowed `n`. Return `True` if the ending square can be reached from the
starting square within the given amount of moves. Keep in mind the chessboard
goes from a1 to h8 (8x8).

### Examples

    bishop("a1", "b4", 2) ➞ True
    
    bishop("a1", "b5", 5) ➞ False
    
    bishop("f1", "f1", 0) ➞ True

### Notes

  * Chessboard is always empty (only the bishop is there).
  * Bishop can move in any direction diagonally.
  * If the starting and ending square are the same, return `True` (even if the move is 0).
  * Square names will always be lowercase and valid.

"""

def bishop(start, end, n):
  
  Black_Squares = [   "a1", "c1", "e1", "g1",
                      "a3", "c3", "e3", "g3",
                      "a5", "c5", "e5", "g5",
                      "a7", "c7", "e7", "g7",
                      "b2", "d2", "f2", "h2",
                      "b4", "d4", "f4", "h4",
                      "b6", "d6", "f6", "h6",
                      "b8", "d8", "f8", "h8"  ]
  
  White_Squares = [   "a2", "c2", "e2", "g2",
                      "a4", "c4", "e4", "g4",
                      "a6", "c6", "e6", "g6",
                      "a8", "c8", "e8", "g8",
                      "b1", "d1", "f1", "h1",
                      "b3", "d3", "f3", "h3",
                      "b5", "d5", "f5", "h5",
                      "b7", "d7", "f7", "h7"  ]
  
  File_Code = "abcdefgh"
  Rank_Code = "12345678"
  
  Pre_Test_A1 = File_Code.index(start[0])
  Pre_Test_A2 = Rank_Code.index(start[1])
  
  Pre_Test_B1 = File_Code.index(end[0])
  Pre_Test_B2 = Rank_Code.index(end[1])
  
  Test_01 = abs(Pre_Test_B1 - Pre_Test_A1)
  Test_02 = abs(Pre_Test_B2 - Pre_Test_A2)
  
  if (n == 0) and (start != end):
    return False
  
  elif (start in Black_Squares) and (end not in Black_Squares):
    return False
  
  elif (start not in Black_Squares) and (end in Black_Squares):
    return False
  
  elif (n == 1) and (Test_01 == Test_02):
    return True
  
  elif (n == 1) and (Test_01 != Test_02):
    return False
  
  else:
    return True

