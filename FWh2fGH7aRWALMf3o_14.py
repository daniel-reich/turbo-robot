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
  if len(string) == 0:
    return ""
  results = recursiveCleave(string, lst)
  if( len(results) == 0 ):
    return "Cleaving stalled: Word not found"
  else:
    return results[0]
def recursiveCleave(string, lst):
  if len(string) == 0:
    return [""]
  potentialBreaks = []
  for endIndex in range(len(string)+1):
    subStr = string[:endIndex]
    if subStr in lst:
      potentialBreaks += [ endIndex ]
  potentialResults = []
  for potentialBreak in potentialBreaks:
    otherHalf = recursiveCleave(string[potentialBreak:], lst)
    for results in otherHalf:
        if( len(results) != 0 ):
          potentialResults += [ string[:potentialBreak] + " " + results ]
        else:
          potentialResults += [ string[:potentialBreak]]
  return potentialResults

