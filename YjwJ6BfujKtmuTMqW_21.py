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

def play_round (P1, P2, P3, P4):
  ptotals = [P1[0]+P1[1],P2[0]+P2[1],P3[0]+P3[1],P4[0]+P4[1]]
  pfirsts = [P1[0],P2[0],P3[0],P4[0]]
  m = min(ptotals)
  if (ptotals.count(m)==1):
    return(('p1' if ptotals[0]==m else 'p2' if ptotals[1]==m 
    else 'p3' if ptotals[2]==m else 'p4'))
  else:
    pfirsts[0] = (7 if ptotals[0] != m else P1[0])
    pfirsts[1] = (7 if ptotals[1] != m else P2[0])
    pfirsts[2] = (7 if ptotals[2] != m else P3[0])
    pfirsts[3] = (7 if ptotals[3] != m else P4[0])
    n = min(pfirsts)
    if (pfirsts.count(n) > 1):
      return ('')
    else:
      return(('p1' if pfirsts[0]==n else 'p2' if pfirsts[1]==n 
      else 'p3' if pfirsts[2]==n else 'p4'))
​
def dice_game(scores):
  players_in = 4
  play_rolls = {'p1':(0,0) ,'p2': (0,0),'p3':(0,0) ,'p4':(0,0)}
  play_in = {'p1': True, 'p2': True, 'p3': True, 'p4': True}
  while players_in > 1:
    play_rolls['p1'] = (scores[0] if play_in['p1']==True else (7,7))
    if play_in['p1']==True : scores.pop(0) 
    play_rolls['p2'] = (scores[0] if play_in['p2']==True else (7,7))
    if play_in['p2']==True : scores.pop(0) 
    play_rolls['p3'] = (scores[0] if play_in['p3']==True else (7,7))
    if play_in['p3']==True : scores.pop(0) 
    play_rolls['p4'] = (scores[0] if play_in['p4']==True else (7,7))
    if play_in['p4']==True : scores.pop(0) 
    loser = play_round(play_rolls['p1'],play_rolls['p2'],play_rolls['p3'],play_rolls['p4'])
    if (loser != ''):
      play_in[loser] = False
      players_in -= 1
  return ('p1' if play_in['p1']==True else 'p2' if play_in['p2']==True 
  else 'p3' if play_in['p3']==True else 'p4' )

