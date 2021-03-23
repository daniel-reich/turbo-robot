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
    last = txt[-1]
    all_else = txt[0:len(txt)-1]
    txt_list = list()
    for word in all_else.split(' '):
        if word[0].lower() in ['a','e','i','o','u']:
            word2 = word+'way'
        else:
            word2 = word[1:]+word[0]+'ay'
        txt_list.append(word2)
    txt_list[0] = txt_list[0].lower().capitalize()
    #txt_list.append(last)
    return " ".join(str(x) for x in txt_list)+last

