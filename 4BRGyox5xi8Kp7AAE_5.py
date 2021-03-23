"""


Create a function that takes a code of chess board square and return his
color.

![Alternative Text](https://edabit-
challenges.s3.amazonaws.com/15694848364196442.jpg)

### Examples

    chess_board("A1") ➞ "black"
    
    chess_board("E5") ➞ "black"
    
    chess_board("D1") ➞ "white"

### Notes

N/A

"""

def chess_board(pole):
  odds = 'aceg'
  cell = int(pole[1])
  if cell%2==0:
    if pole[0] in odds:
      return 'white'
    else:
      return 'black'
  else:
    if pole[0] in odds:
      return 'black'
    else:
      return 'white'

