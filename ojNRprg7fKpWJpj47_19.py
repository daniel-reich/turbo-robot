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
    letters=[]
    fin=[]
    txt= txt.split(' ')
    for a in txt:
        letters.append(a[0])
    for a in reversed(range(0,len(letters)-1)):
        temp=letters[a+1]
        letters[a+1]=letters[a]
        letters[a]=temp
    for a in range(0,len(txt)):
        fin.append(letters[a]+txt[a][1:])
    fin=' '.join(fin)
    return fin

