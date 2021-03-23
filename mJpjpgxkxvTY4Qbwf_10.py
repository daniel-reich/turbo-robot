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
​
    vert_scores=[0]*5
    diag_score1=0
    diag_score2=0
    diag_index1 = -1
    diag_index2 = 5
    for row in board:
        horiz_score=0
        diag_index1+=1
        diag_index2-= 1
​
        for index,item in enumerate(row):
            horiz_score+=((item=="x"))
​
            diag_score1 += (index == diag_index1)*((item=="x"))
            diag_score2 += (index == diag_index2)*((item == "x"))
​
            vert_scores[index]+=(item=="x")
​
            if vert_scores[index]==5 or horiz_score==5 or  diag_score1==5 or  diag_score2==5 :
                return True
​
    return False

