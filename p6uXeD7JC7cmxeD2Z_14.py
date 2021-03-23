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
  leftwin = 0
  rightwin = 0
  for i in games:
    if check(i) == "tie":
      leftwin += 1
      rightwin += 1
    elif check(i) == "left":
      leftwin += 1
    elif check(i) == "right":
      rightwin += 1
  if leftwin > rightwin:
    return "Abigail"
  elif rightwin > leftwin:
    return "Benson"
  else:
    return "Tie"
      
def check(lst):
  if lst[0] == lst[1]:
    return "tie"
  elif lst[0] == "R" and lst[1] == "P":
    return "right"
  elif lst[0] == "P" and lst[1] == "S":
    return "right"
  elif lst[0] == "S" and lst[1] == "R":
    return "right"
  else:
    return "left"

