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
    words = txt.split()
    c_last = words[-1][0]
    word2 = words[-1]
    for i in range(len(words) - 2, -1, -1):
        word1 = words[i]
        word2 = word1[0] + word2[1:]
        words[i+1] = word2
        word2 = word1
    words[0] = c_last + words[0][1:]
    return ' '.join(words)

