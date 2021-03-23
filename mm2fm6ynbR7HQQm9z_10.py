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
  letter = ord(square[0])
  number = int(square[1])
  strings = []
  for num in [-2,-1,1,2]:
    if number + num > 0 and number+num <= 8:
      for l in [-2,-1,1,2]:
        if letter + l >= 65 and letter + l <= 72 and abs(num) != abs(l):
          strings.append(chr(l+letter)+str(number+num))
  return ','.join(strings)

