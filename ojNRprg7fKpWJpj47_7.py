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

def shift_sentence(txt: str) -> str:
    if txt.find(' ') == -1:
        return txt
    l1 = txt.split()
    l2 = l1[:] * 2
    l2 = l2[len(l1) - 1:]
    for i in range(len(l1)):
        if len(l1[i]) > 1:
            l1[i] = l2[i][0] + l1[i][1:]
        else:
            l1[i] = l2[i][0]
    return ' '.join(l1)

