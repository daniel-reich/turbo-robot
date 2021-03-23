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

def dice_game(lst: list) -> str:
    p = ['p1', 'p2', 'p3', 'p4']
    i = 0
    while True:
        temp = [[sum(j), j[0]] for j in lst[i:i+len(p)]]
        i += len(p)
        l = list(zip(*temp))
        x = min(l[0])
        if l[0].count(x) == 1:
            y = l[0].index(x)
            p.pop(y)
        elif l[0].count(x) >= 1:
            z = min(l[1])
            if l[1].count(z) == 1:
                r = l[1].index(z)
                p.pop(r)
        if len(p) == 1:
            return p[0]

