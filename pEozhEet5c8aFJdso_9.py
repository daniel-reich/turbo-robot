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

def midOc(txt):
  count = 0
  countTwo = -1
  
  for ctr in txt:
    countTwo += 1
    if count == 0 and ctr == txt[1]:
      count += 1
    elif count == 1 and ctr == txt[1]:
      return "@ index " + str(countTwo)
    elif txt.count(txt[1]) < 2:
      return "not found"
def findMid(str):
  lstStr = [a for a in str]
  if len(str) % 2 == 0:
    return lstStr[int((len(str)/2)-1)] + lstStr[int(len(str)/2)]
  else:
    return lstStr[int((len(str)/2)-.5)]
def all_about_strings(txt):
  lstTxt = [m for m in txt]
  Attributes = [len(txt),lstTxt[0],lstTxt[-1],findMid(txt),midOc(txt)]
  return Attributes

