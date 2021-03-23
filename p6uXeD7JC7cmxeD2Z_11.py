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

def calculate_score(array):
    Abigail = 0
    Benson = 0
    for i in range(len(array)):
        if (array[i][0] == "R" and array[i][1] == "S") :Abigail += 1
        if (array[i][0] == "S" and array[i][1] == "P") :Abigail += 1
        if (array[i][0] == "P" and array[i][1] == "R") :Abigail += 1
        if (array[i][0] == "S" and array[i][1] == "R") :Benson += 1
        if (array[i][0] == "P" and array[i][1] == "S") :Benson += 1
        if (array[i][0] == "R" and array[i][1] == "P") :Benson += 1
    return 'Tie' if Abigail==Benson else 'Abigail' if Abigail>Benson else 'Benson'

