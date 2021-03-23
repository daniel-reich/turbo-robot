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
    x = 0
    y = 0
    for a in directions:
        if "N" in a:
            x += 1
        elif "W" in a:
            y -= 1
        elif "S" in a:
            x -= 1
        elif "E" in a:
            y += 1
    if x == 0 and y == 0:
        return True
    else:
        return False
print(back_to_home("NENESSWW"))

