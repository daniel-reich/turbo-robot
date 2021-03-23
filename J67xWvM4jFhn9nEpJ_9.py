"""


Make a function that takes a integer, `size`, returns 2D list that is a Magic
Square with side lengths of `size`

A Magic Square is an arrangement of numbers in a square in such a way that the
sum of each row, column, and diagonal is one constant number, the "magic
constant." For this challenge I will be testing with the assumption that your
magic squares are made with whole numbers from 1 - n^2

### Example

    make_magic(3) ➞ [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    # Rows: 2+7+6 = 9+5+1 = 4+3+8 = 15
    # Columns: 2+9+4 = 7+5+3 = 6+1+8 = 15
    # Diagonals: 2+5+8 = 6+5+4 = 15

### Notes

For this challenge I will only be testing with sizes >= 3 as there are no
Magic Squares of size 2 at least as I have described them.

"""

def make_magic(size):
  #Determin what kind of Magic Square we are working with
  return makeOddMagic(size) if (size%2) else makeSEvenMagic(size) if (size%4)  else makeDEvenMagic(size)
​
#Make a Magic Square with an odd size
def makeOddMagic(size):
  square =  [[0 for i in range(size)] for j in range(size)] #Make empty Matrix
  x, y = 0, size//2 #Starting index
  for i in range(1, size**2 + 1):
    square[abs(x)][y] = i
    
    #Check for next index
    if square[abs((x + 1)%-size)][(y + 1)%size] == 0:
      x = (x + 1)%-size
      y = (y + 1)%size
    else:
      x = (x - 1)%-size
      
  return square # Return the finished Magic Square
​
​
​
#Make a Magic Square with a size divisible by 4 
def makeDEvenMagic(size):
  square =  [[0 for i in range(size)] for j in range(size)] #Make empty Matrix
  
  # Starting with the corners and the middle place the index value as at each location 
  cSize = size//4
  
  # Top left
  for i in range(0,cSize):
    for j in range(0,cSize):
      square[i][j] = (i)*size + j+1
      
  # Top right
  for i in range(0,cSize):
    for j in range(size - cSize,size):
      square[i][j] = (i)*size + j+1
      
  # Bottom Left
  for i in range(size - cSize,size):
    for j in range(0,cSize):
      square[i][j] = (i)*size + j+1
      
  # Bottom right
  for i in range(size - cSize,size):
    for j in range(size - cSize,size):
      square[i][j] = (i)*size + j+1
      
  # Mid
  for i in range(cSize, size - cSize ):
    for j in range(cSize, size - cSize):
      square[i][j] = (i)*size + j+1
  
  # Next place the Backwards index as the value at each location that is still empty
  for i in range(size):
    for j in range(size):
      if square[i][j] == 0:
        square[i][j] = size**2 - ((i)*size + j)
  
  return square # Return the finished Magic Square
  
  
​
#Make a Magic Square with an even size that is not divisible by 4   
def makeSEvenMagic(size):
  square =  [[0 for i in range(size)] for j in range(size)] #Make empty Matrix
  
  # Fill the corners with odd magic squares plus an offset
  cSize = size//2
  Temp = makeOddMagic(cSize)
  # Top left
  k = 0
  offSet = 0
  for i in range(0,cSize):
    for j in range(0,cSize):
      square[i][j] = Temp[k//cSize][k%cSize] + offSet
      k += 1
      
  # Bottom right
  k = 0
  offSet = cSize**2
  for i in range(size - cSize,size):
    for j in range(size - cSize,size):
      square[i][j] = Temp[k//cSize][k%cSize] + offSet
      k += 1
        
  # Top right
  k = 0
  offSet = cSize**2*2
  for i in range(0,cSize):
    for j in range(size - cSize,size):
      square[i][j] = Temp[k//cSize][k%cSize] + offSet
      k += 1
  
  # Bottom Left
  k = 0
  offSet = cSize**2*3
  for i in range(size - cSize,size):
    for j in range(0,cSize):
      square[i][j] = Temp[k//cSize][k%cSize] + offSet
      k += 1    
  
  
  # Make some swaps to correct the Magic square
  dSize = cSize//2
  
  #top half of swaps
  for i in range(dSize):
    for j in range(dSize):
      temp1 = square[i][j]
      square[i][j] = square[i + cSize][j]
      square[i + cSize][j] = temp1
      
  #mid swaps
  i = dSize
  for j in range(1, dSize+1):
    temp1 = square[i][j]
    square[i][j] = square[i + cSize][j]
    square[i + cSize][j] = temp1
  
  #top half of swaps
  for i in range(dSize + 1, dSize*2+1):
    for j in range(dSize):
      temp1 = square[i][j]
      square[i][j] = square[i + cSize][j]
      square[i + cSize][j] = temp1
      
  # If the size > 6 make some more swaps    
  dSize -= 1
  
  for i in range(cSize):
    for j in range(size - 1,size - dSize - 1, -1):
      temp1 = square[i][j]
      square[i][j] = square[i + cSize][j]
      square[i + cSize][j] = temp1
  
  return square # Return the finished Magic Square

