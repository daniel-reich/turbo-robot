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
  cadence = ""
  chords = chords[-2:]
  if chords[1]=="I":
    if chords[0]=="V":
      cadence="perfect"
    if chords[0]=="IV":
      cadence="plagal"
  if chords[1]=="V":
    cadence="imperfect"
  if chords[0]=="V" and chords[1]!="I":
    cadence="interrupted"
    
  if cadence=="":
    return("no cadence")
  else:
    return(cadence)
