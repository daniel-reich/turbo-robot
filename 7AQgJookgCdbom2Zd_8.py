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
  tlst = txt.split()
  for i,w in enumerate(tlst):
    up = w[0].isupper()
    w = w.lower()
    punc = w[-1] if not w[-1].isalpha() else ''
    w = w[:-1] if punc else w
    if w[0] in 'aeiou':
      w += 'way'
    else:
      w = w[1:]+w[0]+'ay'
    tlst[i] = (w+punc).capitalize() if up else w+punc
  return ' '.join(tlst)

