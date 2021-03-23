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
  lst = []
  mid = len(txt) // 2
  lst.append(len(txt))
  lst.append(txt[0])
  lst.append(txt[-1])
  if len(txt) % 2 == 0:
    lst.append(txt[mid - 1:mid + 1])
  else:
    lst.append(txt[mid])
  for i in txt:
    if txt.count(i) >= 2:
      lst.append('@ index ' + str(txt.index(i, txt.index(i) + 1)))
      break
  if len(lst) != 5:
      lst.append('not found')
  return lst

