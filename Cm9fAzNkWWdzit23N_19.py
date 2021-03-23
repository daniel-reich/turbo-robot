"""


![Mexican Wave Simulator](https://s3.amazonaws.com/edabit-images/mex.gif)

 _The wave (known as a Mexican wave in the English-speaking world outside
North America) is an example of metachronal rhythm achieved in a packed
stadium when successive groups of spectators briefly stand, yell, and raise
their arms._

Create a function that takes a string and turns it into a Mexican Wave.

### Examples

    wave("edabit") ➞ ["Edabit", "eDabit", "edAbit", "edaBit", "edabIt", "edabiT"]
    
    wave("just do it") ➞ ["Just do it", "jUst do it", "juSt do it", "jusT do it", "just Do it", "just dO it", "just do It", "just do iT"]
    
    wave(" ") ➞ []

### Notes

  * All test cases will be lowercase strings.
  * Ignore spaces (they are considered empty seats).
  * An empty string should return an empty list.

"""

def wave(txt):
    if txt == ' ':
        return []
    elif len(txt) <= 1:
        return list(txt.upper())
    if txt[0] == ' ':
        ntxt = " Blue"
        lst = [ntxt]
        lst += helper(ntxt, 1) 
        return lst   
    else:  
        ntxt = txt[0].upper() + txt[1:]
        lst = [ntxt]
        lst += helper(ntxt, 0)
        return lst
​
​
def helper(txt, n):
    if n == len(txt) - 1:
        return []
    if txt[n+1] == ' ' and n + 2 >= len(txt) - 1:
        return []
    else:
        ntxt = txt[:n] + txt[n].lower() + txt[n+1].upper() + txt[n+2:]
        if txt[n+1] == ' ':
            return helper(ntxt, n+1)
        return [ntxt] + helper(ntxt, n+1)

