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

def knights_jump(square):
  alpha='ABCDEFGH'
  a, k=alpha.find(square[0])+1, int(square[1])
  A=[]
  for i in range(1, 9):
    for j in range(1, 9):
      if (abs(i-k)==2 and abs(j-a)==1) or (abs(i-k)==1 and abs(j-a)==2):
        A.append((j-1, i))
  B=[''.join([alpha[x[0]], str(x[1])]) for x in A]
  return ','.join(B)

