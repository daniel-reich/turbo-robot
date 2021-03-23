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
  res = [0]*5
  res[0] = len(txt)
  res[1] = txt[0]
  res[2] = txt[-1]
  mid = len(txt)//2
  if len(txt)%2==1:
    res[3] = txt[mid]
  else:
    res[3] = txt[mid-1:mid+1]
  pos = -1
  for i in range(2,len(txt)):
    if txt[i]==txt[1]:
      pos=i
      break
  if pos != -1:
    res[4]  = "@ index " + str(pos)
  else:
    res[4] = "not found"
  return res

