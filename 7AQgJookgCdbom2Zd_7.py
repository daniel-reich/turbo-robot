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

from string import punctuation
def pig_latin(txt):
    punc_mark = txt[len(txt) - 1]
    txt = ''.join([x for x in list(txt) if x not in punctuation])
    txt = txt.replace('.', '')
    txt_split = txt.split(' ')
    new_txt = []
    for index, w in enumerate(txt_split):
        if w[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            new_txt.append(w + 'way')
            continue
        if w[0].lower() not in ['a', 'e', 'i', 'o', 'u'] and len(w) == 1:
            new_txt.append(w + 'ay')
            continue
        w_lst = list(w)
        w_lst = [x.lower() for x in w_lst]
        first_letter = w_lst[0]
        w_lst.append(first_letter)
        w_lst = w_lst[1:] + ['ay']
        if index == 0:
            w_lst[0] = w_lst[0].upper()
        w_lst = ''.join(w_lst)    
        new_txt.append(w_lst)
    return ' '.join(new_txt) + punc_mark

