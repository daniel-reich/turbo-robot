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
  lst0 = txt.split()
  lst1 = []
  lst2 = []
  lst3 = []
  lst4 = []
  for i in lst0:
    lst1.append(i[-1]);
    lst2.append(txt.split().index(i))
  
  for i in range(len(lst1)):
    lst3.append(str(lst1[i])+str(lst2[i]))
  lst3 = sorted(lst3)
  for i in lst3:
    lst4.append(lst0[int(i[1:])])
  return " ". join(lst4)

