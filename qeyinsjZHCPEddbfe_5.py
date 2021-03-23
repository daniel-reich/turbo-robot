"""


John is playing a dice game. The rules are as follows.

  1. Roll two dice.
  2. Add the numbers on the dice together.
  3. Add the total to your overall score.
  4. Repeat this for three rounds.

 **But if you roll DOUBLES, your score is instantly wiped to 0 and your game
ends immediately!**

Create a function that takes in a list of tuples as input, and return John's
score after his game has ended.

### Examples

    dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21
    
    dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0
    
    dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27

### Notes

  * Ignore all other tuples in the list if a throw happens to be doubles and go straight to returning `0`.
  * John only has two dice and will always give you outcomes for three rounds.

"""

def dice_game(lst):
    sum = 0
    for rolls in lst:
        if rolls[0] == rolls[1]:
            return 0
        else:
            sum += rolls[0]+rolls[1]
    return sum

