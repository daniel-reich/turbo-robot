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
  whiteEvens = pole[0] in "aceg"
  if int(pole[1]) % 2 == 0:
    return "white" if whiteEvens else "black"
  return "black" if whiteEvens else "white"

