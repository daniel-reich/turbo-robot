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

def shift_sentence(a):
    a = a.split()
    new_list = a[:]
    new_list[0] = a[-1][0] + a[0][1:]
    for i in range(1, len(a)):
        new_list[i] = a[i-1][0] + a[i][1:] 
    return " ".join(new_list)

