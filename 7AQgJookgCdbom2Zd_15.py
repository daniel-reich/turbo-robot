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
    Vowel = ('A','E','I','O','U','a','i','o','u','e')
    special_character = ('?',"!",".")
    text_dict = txt.split()
    new_dict = []
    for word in text_dict:
      if word[0] in Vowel and word[-1] not in special_character:
        new_dict.append(word + "Way")
      elif word[0] not in Vowel and word[-1] not in special_character:
        new_dict.append(word[1:] + word[0] + 'ay')
      elif word[0] not in Vowel and word[-1] in special_character:
        new_dict.append(word[1:-1] + word[0] + 'ay'+ word[-1])
      else:
        new_dict.append(word[:-1] + "Way"+ word[-1])
    a = (' '.join(new_dict))
    return a.lower().capitalize()

