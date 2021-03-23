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
  An=0
  Be=0
  Ch=0
  for i in txt:
    if i=='A':
      An+=1
    elif i=='B':
      Be+=1
    elif i=='C':
      Ch+=1
  return [An,Be,Ch]

