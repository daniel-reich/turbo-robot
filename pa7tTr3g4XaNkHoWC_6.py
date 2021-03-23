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
  words = sentence.split()
  vowels = 'aeiou'
  for i in range(len(words)):
    if words[i][0] in vowels:
      words[i] = words[i] + 'way'
    else:
      while words[i][0] not in vowels:
        words[i] = words[i][1:] + words[i][0]
      words[i] += 'ay'
  return ' '.join(words)

