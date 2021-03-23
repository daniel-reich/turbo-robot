"""


Create a function that takes a string of words and moves the first letter of
each word to the end of it, then adds 'ay' to the end of the word. This is
called "Pig Latin" and it gets more complicated than the rules in this
particular challenge. I've intentionally kept things simple, otherwise this
would turn into an extremely tedious challenge.

  * Move the first letter of each word to the end of the word.
  * Add "ay" to the end of the word.
  * Words starting with a vowel (A, E, I, O, U) simply have "WAY" appended to the end.

### Examples

    pig_latin("Cats are great pets.")
    ➞ "Atscay areway reatgay etspay."
    
    pig_latin("Tom got a small piece of pie.")
    ➞ "Omtay otgay away mallsay iecepay ofway iepay."
    
    pig_latin("He told us a very exciting tale.")
    ➞ "Ehay oldtay usway away eryvay excitingway aletay."

### Notes

Be sure to preserve proper capitalization and punctuation.

"""

import re
def pig_latin(txt):
  a = txt.lower().split()
  empty = []
  vowels = ['a','e','i','o','u','A','E','I','O','U']
  for i in a:
    if i[0] in vowels:
      empty.append(i + 'way')
    else:
      empty.append(i[1:] + i[0] + 'ay')
  b = ' '.join(empty)
  b = re.sub(r'[^\w\s]','',b)
  return b[0].upper() + b[1:] + txt[-1]

