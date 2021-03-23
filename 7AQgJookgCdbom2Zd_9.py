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
  v='aeiou'
  p='.!?,'
  txt=txt.split()
  for i in range(len(txt)):
    if txt[i][0].lower() in v: 
      if txt[i][-1] not in p: txt[i]=txt[i]+'way'
      else: txt[i]=txt[i][:-1]+'way'+txt[i][-1]
    else: 
      if txt[i][-1] not in p: txt[i]=txt[i][1:]+txt[i][0].lower()+'ay'
      else: txt[i]=txt[i][1:-1]+txt[i][0].lower()+'ay'+txt[i][-1]
  txt[0]=txt[0][0].upper()+txt[0][1:]
  return ' '.join(txt)

