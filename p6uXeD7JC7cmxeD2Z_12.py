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
    dict1={'RP':'P','RS':'R','PS':'S','PR':'P','SR':'R','SP':'S'}
    lst1,lst2=[],[]
    for x in games:
        if len(set(x))==len(x):
            if (x.index(dict1["".join(x)]))==1:
                lst2.append("won")
            if (x.index(dict1["".join(x)]))==0:
                lst1.append("won")
    if lst1 or lst2:   
        if lst1==lst2:
          return "Tie" 
        return "Abigail" if lst1.count('won')>lst2.count('won') else "Benson"
    return "Tie"

