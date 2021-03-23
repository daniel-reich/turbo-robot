"""


Create a function that, given a **string** with at least **three characters**
, returns an array of its:

  1. Length.
  2. First character.
  3. Last character.
  4. Middle character, if the string has an odd number of characters. Middle TWO characters, if the string has an even number of characters.
  5. Index of the second occurrence of the second character in the format **"@ index #"** and **"not found"** if the second character doesn't occur again.

### Examples

    all_about_strings("LASA") ➞ [4, "L", "A", "AS", "@ index 3"]
    
    all_about_strings("Computer") ➞ [8, "C", "r", "pu", "not found"]
    
    all_about_strings("Science") ➞ [7, "S", "e", "e", "@ index 5"]

### Notes

N/A

"""

def all_about_strings(txt):
  newlist = []
  newlist.append(len(txt))
  newlist.append(txt[0])
  newlist.append(txt[-1])
  if len(txt) % 2 != 0:
    middle = len(txt) // 2
    newlist.append(txt[middle])
  else:
    middle = len(txt) // 2
    to_add = txt[middle-1] + txt[middle]
    newlist.append(to_add)
  temp = txt[1]
  if txt.count(temp) == 1:
    newlist.append('not found')
    return newlist
  else:
    txt = txt[0:1] + '$' + txt[2:]
    first_index = txt.index(temp)
    newlist.append('@ index {}'.format(first_index))
    return newlist

