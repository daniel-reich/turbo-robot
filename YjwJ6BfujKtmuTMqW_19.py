"""


Four friends are playing a simple dice game (players are denoted p1, p2, p3
and p4). In each round, all players roll a pair of six-sided dice. The player
with the lowest total score is removed. If the lowest score is shared by two
or more players, the player in that group with the lowest score from their
_first_ dice is removed. If the lowest score is still shared (i.e. two or more
players have the same rolls in the same order), then _all_ players roll again.
This process continues until one player remains. Given a list of scores only
(given in player order for each round), return the winning player.

### Example

    dice_game([(6, 2), (4, 3), (3, 4), (5, 4), (3, 5), (1, 5), (4, 3), (1, 5), (1, 5), (5, 6), (2, 2)]) ➞ "p1"
    
                 p1      p2      p3      p4
    Round 1 -> (6, 2), (4, 3), (3, 4), (5, 4)  Player 3 removed.
    Round 2 -> (3, 5), (1, 5),         (4, 3)  Player 2 removed.
    Round 3 -> (1, 5),                 (1, 5)  No lowest score, players roll again.
    Round 4 -> (5, 6),                 (2, 2)  Player 1 wins!

### Notes

N/A

"""

def dice_game(scores):
  score_generator = (score for score in scores)
  players = ['p{}'.format(num) for num in range(1, 5)]
    
  while True:
    if len(players) == 1:
      return players[0]
    
    total_rolls = []
    first_rolls = []
    for player in players:
      roll = next(score_generator)
      total_rolls.append(sum(roll))
      first_rolls.append(roll[0])
​
    if total_rolls.count(min(total_rolls)) == 1:
      players.remove(players[total_rolls.index(min(total_rolls))])
    else:
      check2 = [first_rolls[total_index] if total == min(total_rolls) else 99 for total_index, total in enumerate(total_rolls)]
      print('check2', check2)
      if check2.count(min(check2)) == 1:
        players.remove(players[check2.index(min(check2))])

