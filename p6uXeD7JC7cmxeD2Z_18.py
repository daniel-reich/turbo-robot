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

import numpy as np
def calculate_score(games):
  res = np.array([[0,2,1],[1,0,2],[2,1,0]])
  choice = {"R":0,"P":1,"S":2}
  res2 = {0:"T",1:"A",2:"B"}
  counts = [0,0]
  for game in games:
    temp = res2[res[choice[game[0]]][choice[game[1]]]]
    if temp == "T":
      continue
    elif temp == "A":
      counts[0] += 1
    elif temp == "B":
      counts[1] += 1
  if counts[0] == counts[1]:
    return 'Tie'
  elif counts[0] > counts[1]:
    return "Abigail"
  else:
    return "Benson"

