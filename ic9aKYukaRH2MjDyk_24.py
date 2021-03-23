"""


Create a function that takes a string of words and return a _string_ sorted
alphabetically by the _last_ character of each word.

### Examples

    sort_by_last("herb camera dynamic") ➞ "camera herb dynamic"
    
    sort_by_last("stab traction artist approach") ➞ "stab approach traction artist"
    
    sort_by_last("sample partner autonomy swallow trend") ➞ "trend sample partner swallow autonomy"

### Notes

  * Tests consist of lowercase alphabetic characters (a-z) and spaces.
  * If two words have the same last character, sort by the order they originally appeared.

"""

def sort_by_last(txt):
  collector = dict()
  
  for word in txt.split(' '):
    if word[-1] not in collector.keys():
      collector[word[-1]] = [word]
    else:
      collector[word[-1]] = collector[word[-1]] + [word]
  
  result = list()
  
  for key in sorted(collector.keys()):
    for word in collector[key]:
      result.append(word)
      
  return ' '.join(result)

