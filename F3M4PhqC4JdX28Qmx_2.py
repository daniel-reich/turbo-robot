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
  north = 0
  south = 0
  east = 0
  west = 0
  for i in directions:
    if i == "N":
      north = north + 1
    if i == "S":
      south = south + 1
    if i == "E":
      east = east + 1
    if i == "W":
      west = west + 1
  if (north - south == 0) and (east - west == 0):
    return True
  else:
    return False
  
  print(back_to_home(NNEESSWW))

