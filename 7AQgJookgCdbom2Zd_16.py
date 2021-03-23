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

def pig_latin(txt):
  lc = txt[-1]
  words = txt[:-1].split()
  final = []
  vowels = ['a', 'e', 'i', 'o', 'u']
  for word in words:
    word = word.lower()
    if word[0] in vowels:
      final.append(word+'way')
    else:
      w = word[0]
      final.append(word[1:]+w+'ay')
  pigstring = " ".join(final)
  return pigstring[0].upper()+pigstring[1:]+lc

