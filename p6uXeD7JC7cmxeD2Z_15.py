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
  mat = [
    [0,-1,1],
    [1,0,-1],
    [-1,1,0]
  ]
  myDict = {
    'R':0,
    'P':1,
    'S':2
  }
  sum = 0
  for game in games:
    sum += mat[myDict[game[0]]][myDict[game[1]]]
  if sum > 0:
    return 'Abigail'
  elif sum < 0:
    return 'Benson'
  else:
    return 'Tie'

