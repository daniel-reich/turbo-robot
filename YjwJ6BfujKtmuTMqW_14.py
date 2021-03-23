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
    players = ['p1', 'p2', 'p3', 'p4']
​
    def remve_player(player_index):
        nonlocal scores
        scores = scores[len(players):]
        players.pop(player_index)
​
    while len(players) > 1:
        total_scores = [sum(s) for s in scores[:len(players)]]
        min_score = min(total_scores)
        min_count = total_scores.count(min_score)
        if min_count == 1:
            remve_player(total_scores.index(min_score))
        else:
            first_dice_score = [s[0] for s in scores[:len(players)]]
            min_score = min(first_dice_score)
            min_count = first_dice_score.count(min_score)
            if min_count == 1:
                remve_player(first_dice_score.index(min_score))
            else:
                scores = scores[len(players):]
    return players[0]

