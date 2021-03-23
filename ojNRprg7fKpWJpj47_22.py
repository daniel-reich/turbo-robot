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
    txt = txt.split(' ')
    ans = list(list(i) for i in txt)
    first = ans[0][0]
    for i in range(len(ans)-1):
        ans[i+1][0],first=first,ans[i+1][0]
    ans[0][0]=first
    return " ".join(list("".join(i) for i in ans))

