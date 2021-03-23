"""


In a board game, a player may pick up a card with several left or right facing
arrows, with the number of arrows indicating the number of tiles to move. The
player should move either left or right, depending on the arrow's direction.

Given a list of the arrows contained on a player's cards, return a singular
string of arrowheads that are equivalent to all of the arrowheads.

### Worked Example

    calculate_arrowhead([">>", "<<", "<<<"]) ➞ "<<<"
    
    # >> means to move 2 places right
    # << means to move 2 places left (cancelling out >>)
    # <<< means to move a further 3 places left
    # overall, the movement can be written as <<<

### Examples

    calculate_arrowhead([">>>>", "<", "<", "<"]) ➞ ">"
    
    calculate_arrowhead([">", "<", ">>", "<", "<<<"]) ➞ "<<"
    
    calculate_arrowhead([">>>", "<<<"]) ➞ ""

### Notes

Return an **empty string** if all the arrowheads cancel out.

"""

def calculate_arrowhead(lst):
  string = ''.join(i for i in lst)
  left = string.count('<')
  right = string.count('>')
  return (right - left) * '>' if right > left else (left - right) * '<'

