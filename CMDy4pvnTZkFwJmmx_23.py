"""


Create a class `Sudoku` that takes a **string** as an argument. The string
will contain the numbers of a regular 9x9 sudoku board **left to right and top
to bottom** , with zeros filling up the empty cells.

### Attributes

An instance of the class `Sudoku` will have one attribute:

  * `board`: a list representing the board, with sublits for each **row** , with the numbers as **integers**. Empty cell represented with `0`.

### Methods

An instance of the class `Sudoku` wil have three methods:

  * `get_row(n)`: will return the row in position `n`.
  * `get_col(n)`: will return the column in position `n`.
  * `get_sqr([n, m])`: will return the square in position `n` if only one argument is given, and the square to which the cell in position `(n, m)` belongs to if two arguments are given.

### Example

![Sudoku picture](https://edabit-
challenges.s3.amazonaws.com/sudoku_hard_039.gif)

    game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
    
    game.board ➞ [
      [4, 1, 7, 9, 5, 0, 0, 3, 0],
      [0, 0, 0, 0, 0, 0, 7, 0, 0],
      [0, 6, 0, 0, 0, 7, 0, 0, 0],
      [0, 5, 0, 0, 0, 9, 1, 0, 6],
      [8, 0, 0, 6, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 4, 0, 0],
      [9, 0, 0, 0, 0, 5, 0, 0, 0],
      [0, 0, 0, 4, 3, 0, 0, 0, 0],
      [2, 0, 0, 7, 0, 1, 5, 8, 0]
    ]
    
    game.get_row(0) ➞ [4, 1, 7, 9, 5, 0, 0, 3, 0]
    game.get_col(8) ➞ [0, 0, 0, 6, 0, 0, 0, 0, 0]
    game.get_sqr(1) ➞ [9, 5, 0, 0, 0, 0, 0, 0, 7]
    game.get_sqr(1, 8) ➞ [0, 3, 0, 7, 0, 0, 0, 0, 0]
    game.get_sqr(8, 3) ➞ [0, 0, 5, 4, 3, 0, 7, 0, 1]

### Notes

  * All positions are indexed to 0.
  * All orders are assigned left to right and top to bottom.

"""

class Sudoku:
    
    def __init__(self,values):
        list_index=0
        char_count=0
        inside_list=[]
        self.board=[[]]
        for i in values:
            ##adding values to the outer list
            if char_count == 8:
                inside_list.insert(char_count,int(i))
                if list_index==0:
                    self.board.pop()             
                self.board.insert(list_index,inside_list)
                inside_list=[]
                list_index+=1    
            #adding values into the inner list
            else:
                inside_list.insert(char_count,int(i))
            ##    
            if char_count == 8:
                char_count=0
            else:
                char_count+=1
     
    def get_row(self,row_value):
        return self.board[row_value]
     
    def get_col(self,col):
        col_list=[]
        for i in range(9):
            col_list.append(self.board[i][col])
        return col_list
        
    def get_sqr(self,row,col=100):
        sqr_list=[]
        if ( row == 0 and col==100) or ( row == 0 and col==0) or ( row == 0 and col==1) or ( row == 0 and col==2) or ( row == 1 and col==0) or ( row == 1 and col==1) or ( row == 1 and col==2) or ( row == 2 and col==0) or ( row == 2 and col==1) or (row == 2 and col==2):
            sqr_list=[self.board[0][0],self.board[0][1],self.board[0][2],self.board[1][0],self.board[1][1],self.board[1][2],self.board[2][0],self.board[2][1],self.board[2][2]]
        elif ( row == 1 and col==100) or ( row == 0 and col==3) or ( row == 0 and col==4) or ( row == 0 and col==5) or ( row == 1 and col==3) or ( row == 1 and col==4) or ( row == 1 and col==5) or ( row == 2 and col==3) or ( row == 2 and col==4) or (row == 2 and col==5):
                sqr_list=[self.board[0][3],self.board[0][4],self.board[0][5],self.board[1][3],self.board[1][4],self.board[1][5],self.board[2][3],self.board[2][4],self.board[2][5]]
        elif ( row == 2 and col==100) or ( row == 0 and col==6) or ( row == 0 and col==7) or ( row == 0 and col==8) or ( row == 1 and col==6) or ( row == 1 and col==7) or ( row == 1 and col==8) or ( row == 2 and col==6) or ( row == 2 and col==7) or (row == 2 and col==8):
                sqr_list=[self.board[0][6],self.board[0][7],self.board[0][8],self.board[1][6],self.board[1][7],self.board[1][8],self.board[2][6],self.board[2][7],self.board[2][8]]        
        elif ( row == 3 and col==100) or ( row == 3 and col==0) or ( row == 3 and col==1) or ( row == 3 and col==2) or ( row == 4 and col==0) or ( row == 4 and col==1) or ( row == 4 and col==2) or ( row == 5 and col==0) or ( row == 5 and col==1) or (row == 5 and col==2):
            sqr_list=[self.board[3][0],self.board[3][1],self.board[3][2],self.board[4][0],self.board[4][1],self.board[4][2],self.board[5][0],self.board[5][1],self.board[5][2]]
        elif ( row == 4 and col==100) or ( row == 3 and col==3) or ( row == 3 and col==4) or ( row == 3 and col==5) or ( row == 4 and col==3) or ( row == 4 and col==4) or ( row == 4 and col==5) or ( row == 5 and col==3) or ( row == 5 and col==4) or (row == 5 and col==5):
                sqr_list=[self.board[3][3],self.board[3][4],self.board[3][5],self.board[4][3],self.board[4][4],self.board[4][5],self.board[5][3],self.board[5][4],self.board[5][5]]
        elif ( row == 5 and col==100) or ( row == 3 and col==6) or ( row == 3 and col==7) or ( row == 3 and col==8) or ( row == 4 and col==6) or ( row == 4 and col==7) or ( row == 4 and col==8) or ( row == 5 and col==6) or ( row == 5 and col==7) or (row == 5 and col==8):
                sqr_list=[self.board[3][6],self.board[3][7],self.board[3][8],self.board[4][6],self.board[4][7],self.board[4][8],self.board[5][6],self.board[5][7],self.board[5][8]]
                
        elif ( row == 6 and col==100) or ( row == 6 and col==0) or ( row == 6 and col==1) or ( row == 6 and col==2) or ( row == 7 and col==0) or ( row == 7 and col==1) or ( row == 7 and col==2) or ( row == 8 and col==0) or ( row == 8 and col==1) or (row == 8 and col==2):
            sqr_list=[self.board[6][0],self.board[6][1],self.board[6][2],self.board[7][0],self.board[7][1],self.board[7][2],self.board[8][0],self.board[8][1],self.board[8][2]]
        elif ( row == 7 and col==100) or ( row == 6 and col==3) or ( row == 6 and col==4) or ( row == 6 and col==5) or ( row == 7 and col==3) or ( row == 7 and col==4) or ( row == 7 and col==5) or ( row == 8 and col==3) or ( row == 8 and col==4) or (row == 8 and col==5):
                sqr_list=[self.board[6][3],self.board[6][4],self.board[6][5],self.board[7][3],self.board[7][4],self.board[7][5],self.board[8][3],self.board[8][4],self.board[8][5]]
        elif ( row == 8 and col==100) or ( row == 6 and col==6) or ( row == 6 and col==7) or ( row == 6 and col==8) or ( row == 7 and col==6) or ( row == 7 and col==7) or ( row == 7 and col==8) or ( row == 8 and col==6) or ( row == 8 and col==7) or (row == 8 and col==8):
                sqr_list=[self.board[6][6],self.board[6][7],self.board[6][8],self.board[7][6],self.board[7][7],self.board[7][8],self.board[8][6],self.board[8][7],self.board[8][8]]
        
        return sqr_list

