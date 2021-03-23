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

'''
Rock beats scissors, paper beats rock, scissors beat paper
"Player 1 wins"
"Player 2 wins"
"TIE" (if both inputs are the same)
'''
import numpy as np
def rps(s1, s2):
  if s1 == "rock" and s2 == "scissors":
    return "Player 1 wins"
    
  elif s2 == "rock" and s1 == "scissors":
    return "Player 2 wins"
    
  elif s1 == "paper" and s2 == "rock":
    return "Player 1 wins"
    
  elif s2 == "paper" and s1 == "rock":
    return "Player 2 wins"
    
  elif s1 == "scissors" and s2 == "paper":
    return "Player 1 wins"
    
  elif s2 == "scissors" and s1 == "paper":
    return "Player 2 wins"
    
  elif s1 == s2: 
    return 'TIE'

