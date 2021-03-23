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

def calculate_score(lst):
    a =0
    b =0
    for ab,be in lst:
        if ab=='R':
            if be == 'P':
                b+=1
            if be == 'S':
                a+=1
        if ab == "P":
            if be =='S':
                b+=1
            if be =="R":
                a+=1
        if ab == 'S':
            if be == 'R':
                b+=1
            if be == 'P':
                a+=1
    if a>b:
        return "Abigail"
    if b>a:
        return "Benson"
    if a==b:
        return "Tie"

