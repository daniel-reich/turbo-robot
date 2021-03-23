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
  return ' '.join([pl(i) for i in sentence.split()])
  
def pl(word):
  if word[0] in 'aeiou':
    return word+'way'
  lst = [i for i in range(len(word)) if word[i] in 'aeiou']
  return word[lst[0]:]+word[:lst[0]]+'ay'

