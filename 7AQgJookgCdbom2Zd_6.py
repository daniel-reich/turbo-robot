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
  a = []
  b = txt.lower().split()
  for i in b:
      if i[0] in "aeiou":
          if b[-1]==i: a.append(i[:-1]+"way"+i[-1])
          elif b[0]==i: a.append(i.capitalize()+"way")
          else: a.append(i+"way")
      else:
          if b[-1]==i: a.append((i[1:-1].capitalize()if b[0]==b[-1]else i[1:-1])+i[0]+"ay"+i[-1])
          elif b[0]==i: a.append(i[1:].capitalize()+i[0]+"ay")
          else: a.append(i[1:]+i[0]+"ay")
  return " ".join(a)

