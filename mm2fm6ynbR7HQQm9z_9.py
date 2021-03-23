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

square = 'F4'
def knights_jump(square):
    aa = 'ABCDEFGH'
    board = [
        ['A8','B8','C8','D8','E8','F8','G8','H8'],
        ['A7','B7','C7','D7','E7','F7','G7','H7'],
        ['A6','B6','C6','D6','E6','F6','G6','H6'],
        ['A5','B5','C5','D5','E5','F5','G5','H5'],
        ['A4','B4','C4','D4','E4','F4','G4','H4'],
        ['A3','B3','C3','D3','E3','F3','G3','H3'],
        ['A2','B2','C2','D2','E2','F2','G2','H2'],
        ['A1','B1','C1','D1','E1','F1','G1','H1']
            ]
    moves = []
    r = 8-int(square[1])
    c = aa.index(square[0])
    for i in range(len(board)):
        if i==r:
            continue
        for j in range(len(board[i])):
            if j==c:
                continue
            if abs(i-r)==2 and abs(j-c)==1:
                moves.append((int(board[i][j][1]),board[i][j]))
            if abs(i-r)==1 and abs(j-c)==2:
                moves.append((int(board[i][j][1]),board[i][j]))
    moves.sort()
    out = ''
    for i in moves:
        out = out+','+i[1]
    out2 = out[1:len(out)]
    return out2
knights_jump(square)

