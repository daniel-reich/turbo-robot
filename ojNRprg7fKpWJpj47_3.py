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

def shift_sentence(s):
    '''
    Shifts the 1st letter of each word in sentence s to the next word cyclically to
    the right as above then returns the altered sentence.
    '''
    s = s.split()
    
    return ' '.join([s[i].replace(s[i][0], s[(i-1)%len(s)][0], 1) for i in range(len(s))])

