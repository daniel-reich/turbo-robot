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
  blackfirst = [1,0,1,0,1,0,1,0]
  whitefirst = [0,1,0,1,0,1,0,1]
​
  Chess_map = {'a':blackfirst, 'b':whitefirst,
         'c':blackfirst, 'd':whitefirst,
         'e':blackfirst, 'f':whitefirst,
         'g':blackfirst, 'h':whitefirst,
        }
  code = Chess_map[pole[0]][int(pole[1])-1]
  if code == 1:
    solution = 'black'
  else:
    solution = 'white'
  
  print(solution)
  return solution

