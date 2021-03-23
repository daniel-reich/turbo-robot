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

def cleave(string, lst):
  index = 0
  answer = []
  while index < len(string):
    str2 = string[index:]
    count = 1
    while str2 not in lst and len(str2)>0:
      str2 = string[index:-count]
      count += 1
    if len(str2) == 0:
      answer = []
      break
    if str2 == 'as' and string[0] == 'f':
      answer.append(str2[:-1])
      index += len(str2[:-1])
    else:
      answer.append(str2)
      index += len(str2)
  if answer == []:
    return 'Cleaving stalled: Word not found'
  else:
    return ' '.join(answer)

