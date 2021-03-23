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
  def comp(a, b):
    if a + b in ["RS", "SP", "PR"]:
      return 1
    elif a + b in ["SR", "PS", "RP"]:
      return -1
    else:
      return 0
  v = 0
  for i in games:
    v = v + comp(i[0], i[1])
  if v == 0:
    return "Tie"
  elif v > 0:
    return "Abigail"
  else:
    return "Benson"

