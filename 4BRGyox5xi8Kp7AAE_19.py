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
    line = pole[0]
    coll = int(pole[1])
    if (line in 'aceg' and coll in [1, 3, 5, 7]) or (line in 'bdfh' and coll in [2, 4, 6, 8]):
        return 'black'
    return 'white'

