"""


Abigail and Benson are playing Rock, Paper, Scissors.

Each game is represented by an array of length 2, where the first element
represents what Abigail played and the second element represents what Benson
played.

Given a sequence of games, determine who wins the most number of matches. If
they tie, output "Tie".

  * R stands for Rock
  * P stands for Paper
  * S stands for Scissors

### Examples

    calculate_score([["R", "P"], ["R", "S"], ["S", "P"]]) ➞ "Abigail"
    
    # Benson wins the first game (Paper beats Rock).
    # Abigail wins the second game (Rock beats Scissors).
    # Abigail wins the third game (Scissors beats Paper). 
    # Abigail wins 2/3.
    
    calculate_score([["R", "R"], ["S", "S"]]) ➞ "Tie"
    
    calculate_score([["S", "R"], ["R", "S"], ["R", "R"]]) ➞ "Tie"

### Notes

N/A

"""

def calculate_score(games):
  ans = []
  for i in games:
    abigail = i[0]
    ben = i[1]
    if (abigail == 'P' and ben == 'R') or (abigail == 'R' and ben == 'S') or(abigail == 'S' and ben == 'P'):
      ans.append('A')
    elif (ben == abigail):
      ans.append('T')
    else:
      ans.append('B')
  
  if ans.count('A') > ans.count('B'):
    return 'Abigail'
  elif ans.count('B') > ans.count('A'):
    return 'Benson'
  else:
    return 'Tie'

