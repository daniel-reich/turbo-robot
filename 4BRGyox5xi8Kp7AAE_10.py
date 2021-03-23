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
    col, row = "abcdefgh".index(pole[0]), int(pole[1]) - 1
    return ("black" if row % 2 and col % 2 or (not row % 2 and not col % 2)
            else "white")

