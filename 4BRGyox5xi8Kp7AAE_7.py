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
    x = int(''.join([i for i in pole if i.isdigit()]))
    y = ''.join([i for i in pole if i.isalpha()])
    return 'black' if (ord(y) % 2 == 1 and x % 2 == 1) or (ord(y) % 2 == 0 and x % 2 == 0) else 'white'

