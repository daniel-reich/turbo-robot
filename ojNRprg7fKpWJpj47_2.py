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

def shift_sentence(txt):
  A=txt.split()
  B=[x[0] for x in A]
  C=[x[1:] for x in A]
  D=[B[-1]+C[0]]
  E=[x+y for x, y in zip(B, C[1:])]
  return ' '.join(D+E)

