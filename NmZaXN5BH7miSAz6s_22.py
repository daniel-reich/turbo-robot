"""


An arcade game player wants to climb to the top of the leaderboard and track
their ranking. The game uses Dense Ranking, so its leaderboard works like
this:

  * The player with the highest score is ranked number **1** on the leaderboard.
  * Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

Create a function that takes two lists of integers.

    ranked[[100, 90, 90, 80]]
    player[[70, 80, 105]]

The ranked players will have ranks **1** , **2** , **2** , and **3** ,
respectively. If the player's scores are **70** , **80** and **105** , their
rankings after each game are **4th** , **3rd** , and **1st**. Return
`[[4,3,1]]`.

### Explanation

    climbing_leaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]) ➞ [6, 4, 2, 1]

Alice starts playing with 7 players already on the leaderboard, which looks
like this: ![snapshot1](https://edabit-
challenges.s3.amazonaws.com/1-climbingrank.png)

After Alice finishes game 0, her score is 5 and her ranking is 6:
![snapshot2](https://edabit-challenges.s3.amazonaws.com/2-climbingrank.png)

After Alice finishes game 1, her score is 25 and her ranking is 4:
![snapshot3](https://edabit-challenges.s3.amazonaws.com/3-climbingrank.png)

After Alice finishes game 2, her score is 50 and her ranking is tied with
Caroline at 2: ![snapshot4](https://edabit-
challenges.s3.amazonaws.com/4-climbingrank.png)

After Alice finishes game 3, her score is 120 and her ranking is 1:
![snapshot5](https://edabit-challenges.s3.amazonaws.com/5-climbingrank.png)

### Examples

    climbing_leaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]) ➞ [6, 5, 4, 2, 1]
    
    climbing_leaderboard([80, 80, 80, 75, 70, 60, 60, 60], [70, 72, 78, 88]) ➞ [3, 3, 2, 1]

### Notes

N/A

"""

def climbing_leaderboard(ranked, player):
  quit()

