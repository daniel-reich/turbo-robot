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
    firsts, others = [], []
​
    for word in words:
        firsts.append(word[0])
        others.append(word[1::])
​
    shifted_words = [firsts[i - 1] + others[i] for i in range(len(words))]
    shifted_sentence = ' '.join(shifted_words)
​
    return shifted_sentence

