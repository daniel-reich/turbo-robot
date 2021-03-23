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
  string = "" 
  txt = txt.split() 
  last = txt[-1][0]
  string += txt[0].replace(txt[0][0], txt[-1][0], 1) + ' '
  for i in range(len(txt) - 1):
    string += txt[i+1].replace(txt[i+1][0], txt[i][0], 1) + " "
​
  
  
  
  return string.rstrip()

