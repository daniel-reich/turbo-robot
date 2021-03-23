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

def win_check(match):
​
  if match[0] == match[1]:
    return "Tie"
  if match[0] =="P" and match[1]=="R":
    return True
  if match[0] =="R" and match[1]=="S":
    return True
  if match[0] =="S" and match[1]=="P":
    return True
​
​
  if match[0] =="P" and match[1]=="S":
    return False
  if match[0] =="R" and match[1]=="P":
    return False
  if match[0] =="S" and match[1]=="R":
    return False
  
def calculate_score(games):
  score_Abi=0
  score_Ben=0
  for i in games:
    if win_check(i)==True:
      score_Abi+=1
    if win_check(i)==False:
      score_Ben+=1
    if win_check(i) =="Tie":
      pass
  
  
  if score_Abi>score_Ben:
    return "Abigail"
  if score_Abi<score_Ben:
    return "Benson"
  else:
    return "Tie"

