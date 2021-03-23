"""


Create a function that takes a string (without spaces) and a word list,
cleaves the string into words based on the list, and returns the correctly
spaced version of the string (a sentence). If a section of the string is
encountered that can't be found on the word list, return `"Cleaving stalled:
Word not found"`.

### Examples

    word_list = ["about", "be", "hell", "if", "is", "it", "me", "other", "outer", "people", "the", "to", "up", "where"]
    cleave("ifitistobeitisuptome", word_list) ➞ "if it is to be it is up to me"
    
    cleave("hellisotherpeople", word_list) ➞ "hell is other people"
    
    cleave("hellisotterpeople", word_list) ➞ "Cleaving stalled: Word not found"

### Notes

Words on the `word_list` can appear more than once in the string. The
`word_list` is a reference guide, kind of like a dictionary that lists which
words are allowed.

"""

def matchingWords(string, lst):
  return [w for w in lst if string.startswith(w)]
  
def cleave(string, lst):
  possibles = [(string, [])] # elements are (remaining string, [words])
  while len(possibles) > 0:
    potential = possibles.pop(0)
    matches = matchingWords(potential[0], lst)
    for m in matches:
      wds = potential[1].copy()
      wds.append(m)
      remaining = potential[0][len(m):]
      if len(remaining) == 0:
        return ' '.join(wds)
      possibles.append((remaining, wds))
      print(possibles)
  return 'Cleaving stalled: Word not found'

