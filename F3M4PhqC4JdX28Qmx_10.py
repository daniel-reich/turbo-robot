"""


 **Mubashir** has started his journey from home. Given a string of
`directions` (N=North, W=West, S=South, E=East), he will walk for one minute
in each direction. Determine whether a set of directions will lead him back to
the starting position or not.

### Examples

    back_to_home("EEWE") ➞ False
    
    back_to_home("NENESSWW") ➞ True
    
    back_to_home("NEESSW") ➞ False

### Notes

N/A

"""

def back_to_home(directions):
  N = 0
  S = 0
  W = 0
  E = 0
  for x in directions:
    if x == "N":
      N += 1
    elif x == "S":
      S += 1
    elif x == "W":
      W += 1
    elif x == "E":
      E += 1
  if N == S and W == E:
    return True
  else:
    return False

