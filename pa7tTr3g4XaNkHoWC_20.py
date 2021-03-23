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

vow = lambda x: min( i for i in range(len(x)) if x[i] in 'aeiou' )
pig = lambda x: x+'way' if not vow(x) else x[vow(x):]+x[:vow(x)]+'ay'
pig_latin_sentence = lambda t: ' '.join( pig(w) for w in t.split() )

