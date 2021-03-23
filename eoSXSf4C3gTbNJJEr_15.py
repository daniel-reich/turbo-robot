"""


In music, cadences act as _punctuation_ in musical phrases, and help to mark
the end of phrases. Cadences are the two chords at the end of a phrase. The
different cadences are as follows:

  *  **V** followed by **I** is a _Perfect Cadence_
  *  **IV** followed by **I** is a _Plagal Cadence_
  *  **V** followed by **Any chord other than I** is an _Interrupted Cadence_
  *  **Any chord** followed by **V** is an _Imperfect Cadence_

Create a function where given a chord progression as a list, return the type
of cadence the phrase _ends on_.

### Examples

    find_cadence(["I", "IV", "V"]) ➞ "imperfect"
    
    find_cadence(["ii", "V", "I"]) ➞ "perfect"
    
    find_cadence(["I", "IV", "I", "V", "vi"]) ➞ "interrupted"

### Notes

  * Return strings all in lowercase.
  * Only focus on the last two chords of a progression.
  * Return `"no cadence"` if none of the criterea match up.
  *  **I** is a capital **i** not a lowercase **L**.

"""

def find_cadence(chords):
  y=[]
  for x in chords:
    y.append(x.lower())
  print(y)
​
  if y[-1] == "v":
    return('imperfect') 
  elif y[-2] == "v" and y[-1] == "i":
    return('perfect')
  elif y[-2] == "iv" and y[-1] == "i":
    return('plagal')
  elif y[-2] == "v" and y[-1]!= "i":
    return('interrupted')
  else:
    return('no cadence')
