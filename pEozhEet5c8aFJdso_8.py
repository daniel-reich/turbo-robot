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
  one = len(txt)
  d = int(len(txt)/2) if not len(txt) % 2 else int(len(txt)//2)
  two = txt[0]
  three = txt[-1]
  four = txt[(d-1):(d+1)] if not len(txt) % 2 else txt[len(txt)//2]
  five = "".join(["@ index " + str(i)  for i,v in enumerate(txt) if v == txt[1] and i != 1 ]) if txt.count(txt[1]) > 1 else "not found"
  return [one,two,three,four,five]

