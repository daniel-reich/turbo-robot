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
  wl = {'rock' : 'scissors', 'paper' : 'rock', 'scissors' : 'paper'}
  return 'TIE' if p1 == p2 else 'Player {} wins'.format([1, 2][wl[p2] == p1])

