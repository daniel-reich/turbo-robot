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

def chess_board(p):
  l, n = list(p)
  return 'black' if ord(l) % 2 == int(n) % 2 else 'white'

