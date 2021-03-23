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
  # Length
  lst.append(len(txt))
  # First character
  lst.append(txt[0])
  # Last character
  lst.append(txt[-1])
  # Middle character or middle two characters
  if len(txt) % 2 == 0:
    lst.append(txt[len(txt) // 2 - 1] + txt[len(txt) // 2])
  if len(txt) % 2 != 0:
    lst.append(txt[len(txt) // 2])
  # Index of the second occurence of the second character
  # "@ index #" or "not found"
  txt_check = txt[2:]
  index_count = 2
  for char in txt_check:
    if txt[1] not in txt_check:
      lst.append("not found")
      break
    elif char == txt[1]:
      lst.append("@ index {}".format(index_count))
    index_count += 1
  return lst

