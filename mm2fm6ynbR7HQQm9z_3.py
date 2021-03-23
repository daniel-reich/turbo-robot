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
  a,b = s_to_coor(square)
  ans = []
  for i,j in [[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]:
    x,y = a+i,b+j
    if 0<=x<8 and 0<=y<8:
      ans.append(coor_to_s((x,y)))
      
  return ','.join(sorted(ans, key = lambda s:s[::-1]))
  
​
st = 'ABCDEFGH'
​
s_to_coor = lambda s: (st.index(s[0]), int(s[1])-1)
​
coor_to_s = lambda t: st[t[0]] + str(t[1]+1)

