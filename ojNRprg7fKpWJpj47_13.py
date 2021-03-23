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
    lst=[]
    temp=""
    result=""
    for i in range(0,len(txt)):
        if(txt[i]!=' '):
            temp+=txt[i]
        else:
            lst.append(temp)
            temp=""
    lst.append(temp)
    if(len(lst)==1):
        return lst[0]
    else:
        for i in range(0,len(lst)):
            temp2=""
            for k in range(0,len(lst[i])):
                if(i==0):
                    if(k==0):
                        temp2+=lst[len(lst)-1][0]
                    else:
                        temp2+=lst[i][k]
                else:
                    if(k==0):
                        temp2+=lst[i-1][0]
                    else:
                        temp2+=lst[i][k]
            result+=temp2+" "
    return result[:len(result)-1]

