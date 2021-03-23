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
  if len(txt) % 2 == 0:
    middle1 = int(len(txt) / 2 - 1)
    middle2 = int(middle1 + 2)
  else:
    middle1 = int(len(txt) / 2)
    middle2 = int(middle1 + 1)
  index = txt.find(txt[1],2)
  if index != -1:
    index = "@ index " + str(index)
  else:
    index = "not found"
  return [len(txt), txt[0], txt[-1], txt[middle1:middle2], index]

