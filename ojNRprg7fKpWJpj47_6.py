"""


Given a sentence, create a function which shifts the first letter of each word
to the next word in the sentence (shifting right).

### Examples

    shift_sentence("create a function") ➞ "freate c aunction"
    
    shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"
    
    shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"
    
    shift_sentence("edabit") ➞ "edabit"

### Notes

  * The last word shifts its first letter to the first word in the sentence.
  * All sentences will be given in lowercase.
  * Note how single words remain untouched (example #4).

"""

import numpy as np
def shift_sentence(txt):
    a,b,c=[],[],[]
    for i in txt.split(' '):
        a.append(i[0])
    b=np.roll(a,1)
    for i,j in zip(txt.split(' '),b):
        c.append(j+i[1:])
    return (' '.join(c))

