"""


In a board game, a piece may advance 1-6 tiles forward depending on the number
rolled on a six-sided dice. If you advance your piece onto the **same tile**
as another player's piece, both of you earn a bonus.

Given you and your friend's tile number, create a function that returns if
it's possible to earn a bonus when **you** roll the dice.

### Examples

    possible_bonus(3, 7) ➞ True
    
    possible_bonus(1, 9) ➞ False
    
    possible_bonus(5, 3) ➞ False

### Notes

  * You cannot move backward (which is why example #3 doesn't work).
  * If you are already on the same tile, return `False`, as you would be advancing away.
  * Expect only positive integer inputs.

"""

def possible_bonus(a, b):
  return a<b and a+6>=b

