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
  b=['a','c','e','g']
  w=['d','c','f','h']
  if (p[0] in b and int(p[1])%2!=0) or (p[0] in w and int(p[1])%2==0):
    return 'black'
  else:
    return 'white'

