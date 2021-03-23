"""


Four football teams face each other in a tournament and you must determine the
final classification. Depending on the match result, a team gets a certain
amount of points:

  * A win is worth **3** points.
  * A draw is worth **1** point.
  * A defeat is worth **0** points.

Each team faces another once, for a total of six played games. For each game
the result is provided with the following notation:

    "Team X - X Team"

( _with X being the number of goals scored by both teams_ )

    "A 0 - 1 B" ➞ B wins and gets 3 points, A lose and gets 0 points
    "C 2 - 2 D" ➞ It's a draw, both C and D get 1 point

At the end of the tournament, points are counted for each team. If two or more
teams have the same number of points, two further criteria are applied to
determine who gets the best placement, in the order:

  * The greater number of goals scored.
  * The greater goals difference (goals scored minus goals conceded).

Given a list `lst` containing strings with the results of the six played
games, you have to implement a function that returns a list containing four
lists, one for each team, in the following notation:

    [Team, PT, GS, GD]

  * `Team`: A string, name of the team.
  * `PT`: An integer, points obtained.
  * `GS`: An integer, the sum of scored goals.
  * `GD`: An integer, scored goals minus conceded goals (can be negative).

The main list containing the teams' info must be ordered in such a way as to
present the correct placement of each team as if it were a summary of the
final classification and performance.

### Examples

    tournament_scores(["A 0 - 1 B", "C 2 - 0 D", "B 2 - 2 C", "D 3 - 1 A", "A 2 - 2 C", "B 2 - 0 D"]) ➞ [ [ "B", 7, 5, 3 ], [ "C", 5, 6, 2 ], [ "D", 3, 3, -2 ], [ "A", 1, 3, -3 ] ]
    # Final order is B, C, D, A. All teams have different points, so that a simple descendant sort by points obtained is enough.
    
    tournament_scores(["A 4 - 0 B", "C 2 - 1 D", "B 1 - 0 C", "D 3 - 2 A", "A 1 - 3 C", "B 2 - 1 D"]) ➞ [ [ "C", 6, 5, 2 ], [ "B", 6, 3, -2 ], [ "A", 3, 7, 1 ], [ "D", 3, 5, -1 ] ]
    # Final order is C, B, A, D (C and B have same points, but C has more scored goals than B; A and D have same points but A has more scored goals than D).
    
    tournament_scores(["A 2 - 1 B", "C 3 - 0 D", "B 1 - 1 C", "D 1 - 0 A", "A 3 - 0 C", "B 2 - 4 D"]) ➞ [ [ "A", 6, 5, 3 ], [ "D", 6, 5, 0 ], [ "C", 4, 4, 0 ], [ "B", 1, 4, -3 ] ]
    # Final order is A, D, C, B (A and D have same points and same number of scored goals, but A has a greater goals difference than D).

### Notes

  * For the exercise scope, every given case is working with the given set of instructions, despite in real life football when teams share points, scored goals and goal difference, other criteria are used to determine the placement (sometimes even a coin toss!).

"""

from copy import deepcopy
def sortW(scores):
  sList = []
  rest = deepcopy(scores)
  while len(sList) != len(scores):
    winner, rest = winnerByScore(rest)
    sList.append(winner)
  return sList
def winnerByScore(scores):
  max = 0
  if len(scores) == 1:
    return scores[0], []
  for i, score in enumerate(scores):
    if score[1] > scores[max][1]:
      max = i 
  for i, score in enumerate(scores):
    if i != max and score[1] == scores[max][1]:
      win = winnerByGoal(list(filter(lambda x : x[1] == scores[max][1], scores)))
      for i2, score2 in enumerate(scores):
        if score2[0] == win[0]: max = i2
  return scores[max], [scores[n] for n in range(len(scores)) if n != max] 
def winnerByGoal(scores):
  max = 0
  for i, score in enumerate(scores):
    if score[2] > scores[max][2]:
      max = i 
  for i, score in enumerate(scores):
    if i != max and score[2] == scores[max][2]:
      return winnerByDif(list(filter(lambda x: x[2]==scores[max][2], scores)))
  return scores[max]
def winnerByDif(scores):
  max = 0
  for i, score in enumerate(scores):
    if score[3] > scores[max][3]:
      max = i 
  return scores[max]
def tabulate(t1, s1, t2, s2, mem):
  s1, s2 = int(s1), int(s2)
  if s1 == s2:
    p1 = p2 = 1
  elif s1 > s2:
    p1 = 3
    p2 = 0
  else:
    p1 = 0
    p2 = 3  
  if t1 not in mem.keys():
    mem[t1] = (p1, s1, s1-s2)
  else:
    a,b,c = mem[t1]
    mem[t1] = (p1+a, s1+b, s1-s2+c)
  if t2 not in mem.keys():
    mem[t2] = (p2, s2, s2-s1)
  else:
    a,b,c = mem[t2]
    mem[t2] = (p2+a, s2+b, s2-s1+c)   
  return mem
  
  
def tournament_scores(lst):
  mem = {}
  for entry in lst:
    fst, scd = entry.split(" - ")
    t1, s1 = fst.split()
    s2, t2 = scd.split()
    mem = tabulate(t1, s1, t2, s2, mem)
  result = []
  for team in mem.keys():
    a,b,c = mem[team]
    result.append([team, a, b, c])
  return sortW(result)

