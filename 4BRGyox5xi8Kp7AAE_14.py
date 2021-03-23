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
  
  pole = pole.upper()
  chess_dict = {}
  alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
  
  for i in range(1, 9):
    for letter in alpha[0::2]:
      string = letter+str(i)
      if i % 2 == 0:
        chess_dict[string] = "white"
      else:
        chess_dict[string] = "black"
        
    for letter in alpha[1::2]:
      string = letter+str(i)
      if i % 2 == 0:
        chess_dict[string] = "black"
      else:
        chess_dict[string] = "white"
  location = chess_dict.get(pole)
  return location

