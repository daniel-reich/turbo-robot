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

def check_possibilities(string, lst):
  # There are going to be multiple possibilites, so every time there
  # is more than one option, I'm going to branch and then at the end
  # choose the one that didn't stall
​
  subcomp = ""
  possible = []
  for letter in string:
    subcomp += letter
    if subcomp in lst:
      possible.append(subcomp)
  if len(possible) == 0:
    return False
  return possible
​
def cleave_helper(string, lst, rval, possible):
  if len(string) == 0:
    # made it to the end!
    possible.append(rval)
    return
  word = check_possibilities(string, lst)
  if word == False:
    # rip buddy didn't make it
    possible.append(False)
    return
  for option in word:
    # there are still options
    cleave_helper(string[len(option):], lst, rval + option + " ", possible)
  return
  
def cleave(string, lst):
  rval = ""
  possible = []
  temp = cleave_helper(string, lst, rval, possible)
  for sentence in possible:
    if sentence != False:
      return sentence[:-1]
  return "Cleaving stalled: Word not found"

