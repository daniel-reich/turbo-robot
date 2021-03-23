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
  players = ["p1", "p2", "p3", "p4"]
  player = 0 # player in play
  lplayer = 0 # lowest scoring player for that round
  lscore = 0 # lowest round score
  die = 0 # lowest score first die
  draw = False
​
  for i in scores:
    if player == 0: # sets the new round with first players score
      draw = False
      lscore = sum(i)
      die = i[0]
      lplayer = 0     
    elif sum(i) == lscore: # checks for draws
      if i[0] == die:
        draw = True
      if i[0] < die:
        die = i[0]
        lplayer = player
​
    if sum(i) < lscore: # checks for a lower score
      lscore = sum(i)
      die = i[0]
      lplayer = player
​
    if player == len(players)-1: # ends the reound eliminating player if not lowest draw
      if draw == False or lplayer == len(players)-1:
        del players[lplayer]
      player = 0
    else:
      player += 1
​
  return players[0]

