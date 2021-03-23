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
    players, dice = [1, 2, 3, 4], [(0, 0), (0, 0), (0, 0), (0, 0)]
​
    def remove_player(d, p):
        game = sorted(zip(p, d, [sum(d) for d in d]), key=lambda x: x[2])
        if game[0][2] == game[1][2]:
            game = sorted(zip(p, d, [sum(d) for d in d]), key=lambda x: (x[2], x[1][0]))
            return 0 if game[0][1][0] == game[1][1][0] else game[0][0]
        else:
            return game[0][0]
​
    while len(scores) > 0:
        if len(scores) < len(players):
            pass
        for i in range(0, len(players)):
            dice[i] = scores[0]
            del scores[0]
        dups = remove_player(dice, players)
        if dups > 0:
            players.remove(dups)
        else:
            pass
    return 'p%s' %(int(players[0]))

