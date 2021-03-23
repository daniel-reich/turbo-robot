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
  length = len(txt)
  first = txt[0]
  last = txt[-1]
  mid = ""
  sec_occ = "not found"
  if length % 2 == 0:
    mid += (txt[(length // 2) - 1] + txt[length // 2])
  else:
    mid += txt[length // 2]
  for i in range(2, length):
    if txt[i] == txt[1]:
      sec_occ = "@ index " + str(i)
  return [length, first, last, mid, sec_occ]

