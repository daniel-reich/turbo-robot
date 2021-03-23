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

def tournament_scores(Results):
  
  # Buckets for Statistical Collection on Goals
  
  A_Goals_Scored = 0
  A_Goals_Conceded = 0
  
  B_Goals_Scored = 0
  B_Goals_Conceded = 0
  
  C_Goals_Scored = 0
  C_Goals_Conceded = 0
  
  D_Goals_Scored = 0
  D_Goals_Conceded = 0
  
  # Buckets for Statistical Collection on Wins and Draws Earned
  Wins = []
  Draws = []
  
  # Tallying Goals and Results in While Loop...
  Counter = 0
  Length = len(Results)
  
  while (Counter < Length):
    
    # Pre-Tallying Variables
    
    Match = Results[Counter]
    Blocks = Match.split(" ")
    
    Home_Team = Blocks[0]
    Home_Goals = int(Blocks[1])
    
    Away_Team = Blocks[-1]
    Away_Goals = int(Blocks[-2])
    
    # Establishing Result
    
    if (Home_Goals > Away_Goals):
      Wins.append(Home_Team)
    elif (Away_Goals > Home_Goals):
      Wins.append(Away_Team)
    else:
      Draws.append(Home_Team)
      Draws.append(Away_Team)
    
    # Adjusting Home Team Goals Statistics
    if (Home_Team == "A"):
      A_Goals_Scored += Home_Goals
      A_Goals_Conceded += Away_Goals
      
    elif (Home_Team == "B"):
      B_Goals_Scored += Home_Goals
      B_Goals_Conceded += Away_Goals
      
    elif (Home_Team == "C"):
      C_Goals_Scored += Home_Goals
      C_Goals_Conceded += Away_Goals
    
    elif (Home_Team == "D"):
      D_Goals_Scored += Home_Goals
      D_Goals_Conceded += Away_Goals
    
    else:
      return "ERROR on Home Team Goal Adjustment"
      
    # Adjusting Away Team Goals Statistics
    if (Away_Team == "A"):
      A_Goals_Scored += Away_Goals
      A_Goals_Conceded += Home_Goals
      
    elif (Away_Team == "B"):
      B_Goals_Scored += Away_Goals
      B_Goals_Conceded += Home_Goals
    
    elif (Away_Team == "C"):
      C_Goals_Scored += Away_Goals
      C_Goals_Conceded += Home_Goals
    
    elif (Away_Team == "C"):
      C_Goals_Scored += Away_Goals
      C_Goals_Conceded += Home_Goals
    
    elif (Away_Team == "D"):
      D_Goals_Scored += Away_Goals
      D_Goals_Conceded += Home_Goals
    
    else:
      return "ERROR on Away Team Goal Adjustment"
      
    # Moving to Next Match
    Counter += 1
    
  # Establishing Points Earned
  A_Points = (Wins.count("A") * 3) + (Draws.count("A") * 1)
  B_Points = (Wins.count("B") * 3) + (Draws.count("B") * 1)
  C_Points = (Wins.count("C") * 3) + (Draws.count("C") * 1)
  D_Points = (Wins.count("D") * 3) + (Draws.count("D") * 1)
  
  # Building Lists of Statistics for Each Team
  Batch_A = []
  Batch_A.append("A")
  Batch_A.append(A_Points)
  Batch_A.append(A_Goals_Scored)
  A_Goal_Difference = A_Goals_Scored - A_Goals_Conceded
  Batch_A.append(A_Goal_Difference)
  
  Batch_B = []
  Batch_B.append("B")
  Batch_B.append(B_Points)
  Batch_B.append(B_Goals_Scored)
  B_Goal_Difference = B_Goals_Scored - B_Goals_Conceded
  Batch_B.append(B_Goal_Difference)
  
  Batch_C = []
  Batch_C.append("C")
  Batch_C.append(C_Points)
  Batch_C.append(C_Goals_Scored)
  C_Goal_Difference = C_Goals_Scored - C_Goals_Conceded
  Batch_C.append(C_Goal_Difference)
  
  Batch_D = []
  Batch_D.append("D")
  Batch_D.append(D_Points)
  Batch_D.append(D_Goals_Scored)
  D_Goal_Difference = D_Goals_Scored - D_Goals_Conceded
  Batch_D.append(D_Goal_Difference)
  
  # Building League Table
  League_Table = []
  League_Table.append(Batch_A)
  League_Table.append(Batch_B)
  League_Table.append(Batch_C)
  League_Table.append(Batch_D)
  
  # Sorting League Table and Giving Answer
  League_Table = sorted(League_Table, key = lambda x : (-x[1], -x[2], -x[3], x[0]))
  return League_Table

