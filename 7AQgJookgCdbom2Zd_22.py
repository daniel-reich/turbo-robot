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
def f(w):
  if(re.match(r'^[aeiouAEIOU]',w)):
    return re.sub(r'(\W*)(\w+)(\W*)',r'\1\2way\3',w)
  return re.sub(r'(\W*)(\w)(\w+)(\W*)',r'\1\3\2ay\4',w)
def pig_latin(txt):
  l = txt.split()
  return (" ".join(map(f,l))).capitalize()
print(pig_latin("Cats are great pets."))

