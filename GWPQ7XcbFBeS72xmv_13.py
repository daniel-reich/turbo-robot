"""


Andy, Ben and Charlotte are playing a board game. The three of them decided to
come up with a new scoring system. A player's first initial ("A", "B" or "C")
denotes that player scoring a single point. Given a string of capital letters,
return a list of the players' scores.

For instance, if `ABBACCCCAC` is written when the game is over, then Andy
scored **3 points** , Ben scored **2 points** , and Charlotte scored **5
points** , since there are 3 instances of letter A, 2 instances of letter B,
and 5 instances of letter C. So the list `[3, 2, 5]` should be returned.

### Examples

    calculate_scores("A") ➞ [1, 0, 0]
    
    calculate_scores("ABC") ➞ [1, 1, 1]
    
    calculate_scores("ABCBACC") ➞ [2, 2, 3]

### Notes

If given an empty string as an input, return `[0, 0, 0]`.

"""

def calculate_scores(txt):
  a = 0
  b = 0
  c = 0
  for x in txt:
    if x == 'A':
      a += 1
    elif x == 'B':  
      b += 1
    elif x == 'C':  
      c += 1
  score = [a, b, c]
  return score

