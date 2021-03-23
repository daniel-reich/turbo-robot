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

def knights_jump(s):
  a = 'ABCDEFGH'
  n = '12345678'
  x,y = a.index(s[0]),n.index(s[1])
  ret = []
  if x>1:
    if y>0: ret.append(a[x-2]+n[y-1])
    if y<7: ret.append(a[x-2]+n[y+1])
  if x<6:
    if y>0: ret.append(a[x+2]+n[y-1])
    if y<7: ret.append(a[x+2]+n[y+1])
  if y>1:
    if x>0: ret.append(a[x-1]+n[y-2])
    if x<7: ret.append(a[x+1]+n[y-2])
  if y<6:
    if x>0: ret.append(a[x-1]+n[y+2])
    if x<7: ret.append(a[x+1]+n[y+2])
  return ','.join(sorted(ret,key=lambda i:i[1]))

