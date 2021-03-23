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
  st2=""
  res=""
  for i in txt:
      if not i in ['.','!']:
          st2+=i
  lst=st2.split(" ")
  ll=[]
  for i in lst:
      if not i[0].lower() in ['a','e','i','o','u']:
          ll.append(i[1:]+i[0].lower()+'ay')
      else:
          ll.append(i+'way')
  st3=" ".join(ll)
  for i in range(len(st3)):
      if i==0:
          res+=st3[i].upper()
      else:
          res+=st3[i]
  if len(lst)>1:
    return res+'.'
  else:
    return res+'!'

