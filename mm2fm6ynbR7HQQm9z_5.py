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

def knights_jump(position):
    letter, number = position
    number = int(number)
    pos_jump = []
    #big if block
    if ord(letter) >= 66 and number >= 3: pos_jump.append("{}{}".format(chr(ord(letter) - 1), number - 2))
    if ord(letter) <= 71 and number >= 3: pos_jump.append("{}{}".format(chr(ord(letter) + 1), number - 2))
    if ord(letter) >= 67 and number >= 2: pos_jump.append("{}{}".format(chr(ord(letter) - 2), number - 1))
    if ord(letter) <= 70 and number >= 2: pos_jump.append("{}{}".format(chr(ord(letter) + 2), number - 1))
    if ord(letter) >= 67 and number <= 7: pos_jump.append("{}{}".format(chr(ord(letter) - 2), number + 1))
    if ord(letter) <= 70 and number <= 7: pos_jump.append("{}{}".format(chr(ord(letter) + 2), number + 1))
    if ord(letter) >= 66 and number <= 6: pos_jump.append("{}{}".format(chr(ord(letter) - 1), number + 2))
    if ord(letter) <= 71 and number <= 6: pos_jump.append("{}{}".format(chr(ord(letter) + 1), number + 2))
    return ",".join(pos_jump)

