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
  sentence, vowels = sentence.split(), 'aeiou'
  v_count = [[y.index(x) for x in y if x in vowels][0] for y in sentence]
  return ' '.join([x[0] + 'way' if x[1] == 0 
  else x[0][x[1]:] + x[0][:x[1]] + 'ay' for x in zip(sentence, v_count)])

