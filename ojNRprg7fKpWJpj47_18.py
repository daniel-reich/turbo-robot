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
    first_letter = [a[0] for a in txt.split(' ')]
    first_letter_new_index =  list(first_letter[-1]) + first_letter[0:len(first_letter)-1]
    other_letters = [a[1:] for a in txt.split(' ')]
    return ' '.join([''.join(a) for a in list(zip(first_letter_new_index, other_letters))])

