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
    str=""
    drk=txt.split()
    d=[]
    p=[]
  
    for i in drk:
        d.append(i[0])
        p.append(i[1:])
    for a in range(len(d)):
        if a==0:
            str+=d[-1]+p[a]+""
       
       
        else:
            str=str+" "+d[a-1]+p[a]+""
         
             
    return str

