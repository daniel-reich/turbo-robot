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
    x,y=[],''
    txt=txt.split()
    for word in txt:
        x.append(word[0])
    b=txt[0]
    c=x[-1]+b[1::]
    x1=x[0:-1]
    y+=c
    for word in txt[1::]:
        i=x.pop(0)
        d=i+word[1::]
        y+=' '+d        
    return y

