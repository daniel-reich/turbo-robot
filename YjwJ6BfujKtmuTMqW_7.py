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
  p = ['p1', 'p2', 'p3', 'p4']
  scrs_iter = iter(scores)
  
  def value(p): # value sutiable to compare/sort
    a, b = p[1][0], p[1][1]
    return (a+b)*7 +a
    
  while len(p) > 1:
    # play round
    rnd = list(zip(p, scrs_iter)) # list of (p, (x, y))
    #sort players
    rnd = sorted(rnd, key=value)
    if value(rnd[0]) == value(rnd[1]): continue
    p.remove(rnd[0][0])
  return p[0]

