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
  ans=[]
  for item in lst:
    if item and '7' not in item:
      item+='7'
      ans.append(item)
      flag=1
    else:
      ans.append(item)
  return ans

