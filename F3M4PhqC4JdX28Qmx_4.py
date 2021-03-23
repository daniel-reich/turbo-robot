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
  countN = 0
  countS = 0
  countE = 0
  countW = 0
  for let in directions:
        if let == 'N':
            countN = countN + 1
        if let == 'S':
            countS = countS + 1
        if let == 'E':
            countE = countE + 1            
        if let == 'W':
            countW = countW + 1
  if countN == countS and countE == countW:
        return True
  else:
        return False

