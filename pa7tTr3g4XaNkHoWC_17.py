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

import re
def pig_latin_sentence(sentence):
  res = []
  for word in sentence.split():
    vp = re.search('[aeiou]', word).start()
    if vp:
      res.append(word[vp:] + word[:vp] + 'ay')
    else:
      res.append(word + 'way')
  return ' '.join(res)

