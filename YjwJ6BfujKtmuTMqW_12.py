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
    while len(players) > 1:
        L = []
        for p in players:
            d1, d2 = scores.pop(0)
            L.append([p, d1 + d2, d1])
        L.sort(key=lambda x: (-x[1], -x[2]))
        if L[-2][1] > L[-1][1]:
            # one player has unique lowest total and is eliminated:
            players.remove(L[-1][0])
        elif L[-2][2] > L[-1][2]:
            # tie for lowest total but unique first rolls:
            players.remove(L[-1][0])   
    return players[0]

