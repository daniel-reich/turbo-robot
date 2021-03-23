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
  v = 'aieuo' ; L = []
  for w in sentence.split():
    if w[0] in v: L.append(w+'way')
    else:
      for i in w:
        if i in v:
          L.append(w[w.index(i):]+w[:w.index(i)]+'ay')
          break
  return " ".join(L)

