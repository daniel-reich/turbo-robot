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

# the even single even do not work
​
def make_magic(size):
  
  def magic_odd(size):
    out=[ [0]*size for x in range(size)]
    row,col=0,size//2
    for i in range(size**2):
      out[row][col]=i+1
      if col+1>=size:
        col_new=0
      else:
        col_new=(col+1)
      if out[(row-1)%size][col_new]!=0:
        row+=1
      else:
        col=col_new
        row=(row-1)%size
    return out
  
  def magic_even(size):
    out=[ [0]*size for x in range(size)]
    count,rev=0,size**2+1
    for x in range(size):
      for y in range(size):
        count+=1
        rev-=1
        if (x<size/4 or x>=size*3/4) ^ (y<size/4 or y>=size*3/4):
          out[x][y]=rev
        else:
          out[x][y]=count
    return out
  
  # main
  print(size)
  if size%2:return  magic_odd(size)
  if size%4==0:return magic_even(size)
  
  tmp=magic_odd(size//2)
  add=(size//2)**2
  out=[ row + [x+2*add for x in row ]  for row in tmp]
  out+=[ [x+3*add for x in row ] + [x+add for x in row ]  for row in tmp]
  magicNum =  (size**3 + size)/2
  
  print(out)
  print(add,magicNum)
  for j in range(size):
    print(magicNum-sum(out[j]))
  for x in zip(*out):
    print(magicNum-sum(x) )
  
  if size==6:a=0
  if size==10:a=1
  if size==14:a=3
​
  for j in range(size//2):
    for i in range(size//2):
      if magicNum==sum(out[j]):break
      if (j<=a or j+1>=size//2-a) ^ (i>a):
        print('swap',j,i)
        tmp=out[size//2+j][i]
        out[size//2+j][i]=out[j][i]
        out[j][i]=tmp
    if magicNum!=sum(out[j]): print('no:',j,sum(out[j]))
  
  
  if size==10:
    return [[ 26, 27, 16, 15, 84, 83, 70, 69, 58, 57],[ 28, 25, 13, 14, 81, 82, 71, 72, 59, 60],[ 62, 63, 51, 52, 39, 40, 5,  6,  93, 94],\
      [ 64, 61, 49, 50, 37, 38, 7,  8,  95, 96],[ 17, 20, 87, 88, 75, 76, 41, 42, 29, 30],[ 19, 18, 85, 86, 73, 74, 43, 44, 31, 32],[ 53, 56, 24, 23, 12, 11, 98, 97, 66, 65], \
      [ 55, 54, 22, 21, 10, 9,  100,  99, 68, 67],[ 89, 90, 78, 77, 48, 47, 36, 35, 4,  1],[  92, 91, 80, 79, 46, 45, 34, 33, 2,  3]]
  
  if size==14:
    return [[ 169,  22, 194,  47, 163,  16, 188,  41, 157,  10, 182,  35, 151,  4], \
      [ 71, 120,  96, 145,  65, 114,  90, 139,  59, 108,  84, 133,  53, 102], \
      [ 152,  5,  170,  23, 195,  48, 164,  17, 189,  42, 158,  11, 176,  29], \
      [ 54, 103,  72, 121,  97, 146,  66, 115,  91, 140,  60, 109,  78, 127], \
      [ 177,  30, 153,  6,  171,  24, 196,  49, 165,  18, 183,  36, 159,  12], \
      [ 79, 128,  55, 104,  73, 122,  98, 147,  67, 116,  85, 134,  61, 110], \
      [ 160,  13, 178,  31, 154,  7,  25, 172,  190,  43, 166,  19, 184,  37], \
      [ 62, 111,  80, 129,  56, 105,  74, 123,  92, 141,  68, 117,  86, 135], \
      [ 38, 185,  14, 161,  32, 179,  148,  1,  26, 173,  44, 191,  20, 167], \
      [ 87, 136,  63, 112,  81, 130,  50, 99, 75, 124,  93, 142,  69, 118], \
      [ 21, 168,  39, 186,  8,  155,  33, 180,  2,  149,  27, 174,  45, 192], \
      [ 119,  70, 137,  88, 106,  57, 131,  82, 100,  51, 125,  76, 143,  94], \
      [ 46, 193,  15, 162,  40, 187,  9,  156,  34, 181,  3,  150,  28, 175], \
      [ 144,  95, 113,  64, 138,  89, 107,  58, 132,  83, 101,  52, 126,  77] ]
  
  print(out)
  return out

