"""


Create a function which creates a square dartboard of side length `n`. The
value of a number should increase, the closer it is to the centre of the
board.

### Examples

    make_dartboard(3) ➞ [
      111,
      121,
      111
    ]
    
    make_dartboard(8) ➞ [
      11111111,
      12222221,
      12333321,
      12344321,
      12344321,
      12333321,
      12222221,
      11111111
    ]
    
    make_dartboard(5) ➞ [
      11111,
      12221,
      12321,
      12221,
      11111
    ]

### Notes

If the size given is an even number, the centre should be made up of the 4
highest values.

"""

def make_dartboard(n):
  if n==1:return [1]
  w=[[0]*n for _ in range(n)]
  for k in range(1,int(n/2)+1):
   for i in range(n):
    for j in range(n):
     if i==n-k or j==n-k or i==k-1 or j==k-1:
         if w[i][j]==0:
                w[i][j]=k
  if n%2!=0: w[k][k]=k+1
  return [int("".join([str(j) for j in i])) for i in w]

