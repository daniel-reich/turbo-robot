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

def dice_game(*die):
    all_dices = (die[0])
    players = ["p1", "p2", "p3", "p4"]
    while len(players) > 1:
        dice_dict = {}
        for i in range(len(players)):
            dice_dict[players[i]] = all_dices[i]
        all_dices = all_dices[len(players):]
        dice_sum_dict = {}
        for player in dice_dict:
            dice_sum_dict[player] = dice_dict[player][0] + dice_dict[player][1]
        min_dice = min(dice_sum_dict.values())
        same_score = {}
        for player in dice_sum_dict:
            if dice_sum_dict[player] == min_dice:
                same_score[player] = dice_dict[player][0]
        min_1st_dice = min(same_score.values())
        min_count = 0
        for player in same_score:
            if same_score[player] == min_1st_dice:
                loser = player
                min_count += 1
        if min_count == 1:
            players.remove(loser)
    winner = players[0]
    return (winner)

