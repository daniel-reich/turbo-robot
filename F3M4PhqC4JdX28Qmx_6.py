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
  direct_n = directions.count("N")
  direct_e = directions.count("E")
  direct_w = directions.count("W")
  direct_s = directions.count("S")
  if direct_s == direct_n and direct_e == direct_w :
    return True
  else:
    return False

