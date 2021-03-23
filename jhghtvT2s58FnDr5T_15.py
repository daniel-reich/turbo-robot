"""


Create a function which concantenates the number **7** to the end of every
chord in a list. Ignore all chords which already end with 7.

### Examples

    jazzify(["G", "F", "C"]) ➞ ["G7", "F7", "C7"]
    
    jazzify(["Dm", "G", "E", "A"]) ➞ ["Dm7", "G7", "E7", "A7"]
    
    jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"]) ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
    
    jazzify([]) ➞ []

### Notes

  * Return an empty list if the given list is empty.
  * You can expect all the tests to have valid chords.

"""

def jazzify(lst):
  newlist = []
  for eachitem in lst:
    if eachitem[-1] == '7':
      newlist.append(eachitem)
    else:
      x = '{}7'.format(eachitem)
      newlist.append(x)
  return newlist

