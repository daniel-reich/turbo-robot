"""


You are given a list of scores. The even-indexed numbers are your scores at
each turn. The odd-indexed numbers are your opponent's scores.

Create a function that turns this list of scores into a list of who is
currently winning.

To illustrate (You - `Y`, Opponent - `O`):

    Scores: [5, 15, 17, 35, 16, 40, 66, 12, 10, 9]
    
    Y scores: [5, 17, 16, 66, 10]
    O scores: [15, 35, 40, 12, 9]
    
    Y cumulative scores: [5, 22, 38, 104, 114]
    O cumulative scores: [15, 50, 90, 102, 111]
    
    Who is currently winning: ["O", "O", "O", "Y", "Y"]

### Examples

    currently_winning([10, 10, 22, 30, 5, 40]) ➞ ["T", "O", "O"]
    
    currently_winning([5, 1, 2, 10]) ➞ ["Y", "O"]
    
    currently_winning([10, 10, 5, 5, 2, 2, 1, 3, 100, 5]) ➞ ["T", "T", "T", "O", "Y"]

### Notes

Write "T" if there is a tie at that point in the game.

"""

def currently_winning(scores):
  m=scores[::2]
  o=scores[1::2]
  return ['Y' if sum(m[:x+1])>sum(o[:x+1]) else 'T' if sum(m[:x+1])==sum(o[:x+1]) else 'O' for x in range(len(m))]

