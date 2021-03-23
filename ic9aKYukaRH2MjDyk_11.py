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
  lst = txt.split()
  map = {}
  for str in lst:
    key = getUniqueKey(str[-1], map)
    map[key] = str
  strsorted  = ""
  for key in sorted(map):
    strsorted += " " + map[key]
  return strsorted[1:]
​
def getUniqueKey(str, map):
  if str in map:
    return getUniqueKey(str+str, map)
  else:
    return str

