"""


Write a function that converts a sentence into pig latin.

Rules for converting to pig latin:

  * For words that begin with a vowel (a, e, i, o, u), add "way".
  * Otherwise, move all letters before the first vowel to the end and add "ay".
  * For simplicity, no punctuation will be present in the inputs.

### Examples

    pig_latin_sentence("this is pig latin") ➞ "isthay isway igpay atinlay"
    
    pig_latin_sentence("wall street journal") ➞ "allway eetstray ournaljay"

### Notes

N/A

"""

def pig_latin_sentence(s):
  l=[]
  for x in s.split():
    if x[0]in'aeiou':w=x+'way'
    else:
      w=''
      for i,y in enumerate(x):
        if y not in'aeiou':w+=y
        else:w=x[i:]+w+'ay';break
    l.append(w)
  return' '.join(l)

