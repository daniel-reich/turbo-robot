"""


Create a function which simulates the game "rock, paper, scissors". The
function takes the input of both players (rock, paper or scissors), first
parameter from first player, second from second player. The function returns
the result as such:

  * "Player 1 wins"
  * "Player 2 wins"
  * "TIE" (if both inputs are the same)

The rules of rock, paper, scissors, if not known:

  * Both players have to say either "rock", "paper" or "scissors" at the same time.
  * Rock beats scissors, paper beats rock, scissors beat paper.

### Examples

    rps("rock", "paper") ➞ "Player 2 wins"
    
    rps("paper", "rock") ➞ "Player 1 wins"
    
    rps("paper", "scissors") ➞ "Player 2 wins"
    
    rps("scissors", "scissors") ➞ "TIE"
    
    rps("scissors", "paper") ➞ "Player 1 wins"

### Notes

Try to use a numpy array as a lookup table instead of if-constructions.

"""

def rps(p1, p2):
    if (p1 == "rock" and p2 == "paper") or (p1 == "paper" and p2 == "scissors") or (p1 == "scissors" and p2 == "rock"):
        return "Player 2 wins"
    elif (p2 == "rock" and p1 == "paper") or (p2 == "paper" and p1 == "scissors") or (p2 == "scissors" and p1 == "rock"):
        return "Player 1 wins"
    else:
        return "TIE"

