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

def pig_latin_sentence(sentence):
  res=[]
  for w in sentence.split():
    if w[0] in 'aeiou':res+=[w+'way']
    else:
      while not w[0] in 'aeiou':
        w=w[1:]+w[0]
      res+=[w+'ay']
  return ' '.join(res)

