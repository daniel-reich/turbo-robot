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

def rps(p1,p2):
  if len(p1) == len(p2):
    return "It's a draw"
  p1_winning_stuations = [("Paper", "Rock"), ("Rock", "Scissors"), ("Scissors", "Paper")]
  if (p1,p2) in p1_winning_stuations:
    return "The winner is p1"
  else:
    return "The winner is p2"

