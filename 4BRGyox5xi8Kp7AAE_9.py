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
  x=pole[:1]
  y=pole[1:]
  if ord(x) % 2 == 1:
    if int(y) % 2 == 1:
      return('black')
    else:
      return('white')
  elif ord(x) % 2 == 0:
    if int(y) % 2 == 0:
      return('black')
    else:
      return('white')

