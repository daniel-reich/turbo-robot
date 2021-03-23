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
  a = txt.split(' ')
  final_list = []
  for i in range(len(a)):
    last_char = a[i][-1]
    final_list.append([i, last_char, a[i]])
  final_list.sort(key=lambda x: x[1])
  items = [el[2] for el in final_list]
  return ' '.join(items)

