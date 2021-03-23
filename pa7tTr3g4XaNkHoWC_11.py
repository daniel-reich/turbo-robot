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

def latin(word):
  for index, letter in enumerate(word):
    if letter in 'aeiou':
      break
  return word[index:] + word[:index] + 'ay'
​
​
def pig_latin_sentence(sentence):
  return ' '.join(
    word + 'way' if word[0] in 'aeiou' else latin(word)
    for word in sentence.split()
  )

