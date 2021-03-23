"""


You're given a string of words. You need to find the word "Nemo", and return a
string like this: `"I found Nemo at [the order of the word you find nemo]!"`.

If you can't find Nemo, return `"I can't find Nemo :("`.

### Examples

    find_nemo("I am finding Nemo !") ➞ "I found Nemo at 4!"
    
    find_nemo("Nemo is me") ➞ "I found Nemo at 1!"
    
    find_nemo("I Nemo am") ➞ "I found Nemo at 2!"

### Notes

  * `! , ? .` are always separated from the last word.
  * Nemo will always look like _Nemo_ , and not _NeMo_ or other capital variations.
  *  _Nemo's_ , or anything that says _Nemo_ with something behind it, doesn't count as _Finding Nemo_.
  * If there are multiple _Nemo's_ in the sentence, only return for the first one.

"""

def find_nemo(sentence):
  words = sentence.split(' ')
  if ('Nemo' in words):
    return 'I found Nemo at ' + str(words.index('Nemo') + 1) +'!'
  return 'I can\'t find Nemo :('

