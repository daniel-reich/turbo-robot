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

#Length.
#First character.
#Last character.
#Middle character, if the string has an odd number of characters. 
# Middle TWO characters, if the string has an even number of characters.
#Index of the second occurrence of the second character in the format 
# "@ index #" and "not found" if the second character doesn't occur again.
​
def all_about_strings(txt):
  out = []
  out.append(len(txt))
  out.append(txt[0])
  out.append(txt[-1])
  if len(txt) % 2 == 0:
    m = len(txt)//2
    out.append(txt[m-1:m+1])
  else:
    out.append(txt[len(txt)//2])
  if txt[1] in txt[2:]:
    out.append('@ index {}'.format(txt.index(txt[1], 2)))
  else:
    out.append('not found')
  return out

