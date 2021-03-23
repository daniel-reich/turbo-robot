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
  Abi, Ben = 0, 0
  for i in games:
    if i[0]==i[1]: continue
    if (i[0]=='R' and i[1]=='S') or (i[0]=='P' and i[1]=='R') or (i[0]=='S' and i[1]=='P'):
      Abi += 1
    else:
      Ben += 1
      
  if Abi == Ben:
    return 'Tie'
  elif Abi > Ben:
    return "Abigail"
  else:
    return "Benson"

