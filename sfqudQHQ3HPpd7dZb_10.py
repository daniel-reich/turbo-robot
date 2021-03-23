"""


Create a function which takes two strings (`p1` and `p2` ⁠— which represent
player 1 and 2) as arguments and returns a string stating the winner in a game
of _Rock, Paper, Scissors_.

Each argument will contain a single string: `"Rock"`, `"Paper"`, or
`"Scissors"`. Return the winner according to the following rules:

  *  **Rock** beats **Scissors**
  *  **Scissors** beats **Paper**
  *  **Paper** beats **Rock**

If `p1` wins, return the string `"The winner is p1"`. If `p2` wins, return the
string `"The winner is p2"` and if `p1` and `p2` are the same, return `"It's a
draw"`.

### Examples

    rps("Rock", "Paper") ➞ "The winner is p2"
    
    rps("Scissors", "Paper") ➞ "The winner is p1"
    
    rps("Paper", "Paper") ➞ "It's a draw"

### Notes

All inputs will be valid strings.

"""

def rps(p1, p2):
    retstr = 'The winner is '
    if p1 == p2:
        return 'It\'s a draw'
    elif p1 == 'Rock' and p2 == 'Scissors':
        return retstr+'p1'
    elif p1 == 'Paper' and p2 == 'Rock':
        return retstr+'p1'
    elif p1 == 'Scissors' and p2 == 'Paper':
        return retstr+'p1'
    elif p2 == 'Rock' and p1 == 'Scissors':
        return retstr+'p2'
    elif p2 == 'Paper' and p1 == 'Rock':
        return retstr+'p2'
    elif p2 == 'Scissors' and p1 == 'Paper':
        return retstr+'p2'
    # this is pretty clunky, prone to misspellings (for me)
    # looking forward to seeing other solutions

