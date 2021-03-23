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
  players,j=4,0
  players_out=[]
  p=[1,2,3,4]
  while (j < len(scores)):
    minn=(100,100)
    again=False
    k=0
    for i in range (j,j+players):
      if sum(scores[i]) <= sum((minn)):
        if sum(scores[i]) == sum((minn)):
          if scores[i][0]==minn[0]:
            again=True
          else:
            if scores[i][0]<minn[0]:
              minn = scores[i]
              index=p[k]
              again=False
        else:
          minn = scores[i]
          index=p[k]
          again=False
      k+=1
    j=j+players
    if not (again):
      players-=1
      p.remove(index)
      players_out.append('p'+ str(index))
  return ['p'+str(i) for i in range(1,5) if 'p'+str(i) not in players_out][0]

