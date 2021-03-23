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
  def l8r_shift(w1, w2):
    return w1[0] + w2[1:]
​
  words = txt.split()
  words.append(words[0])
​
  new_words = []
​
  for n in range(len(words) - 1):
    w1 = words[n]
    w2 = words[n+1]
​
    new_words.append(l8r_shift(w1, w2))
  
  new_words_formatted = [new_words[-1]] + new_words[:-1]
​
  return ' '.join(new_words_formatted)

