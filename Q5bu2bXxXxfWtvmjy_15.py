"""


Given a string of letters in the English alphabet, return the letter that's
missing from the string. The missing letter will make the string be in
alphabetical order (from A to Z).

If there are no missing letters in the string, return `"No Missing Letter"`.

### Examples

    missing_letter("abdefg") ➞ "c"
    
    missing_letter("mnopqs") ➞ "r"
    
    missing_letter("tuvxyz") ➞ "w"
    
    missing_letter("ghijklmno") ➞ "No Missing Letter"

### Notes

The given string will never have more than one missing letter.

"""

import string
def missing_letter(txt):
  txt = sorted(txt)
  lowercase = list(string.ascii_lowercase)
  first_index = lowercase.index(txt[0])
  y = lowercase[first_index: first_index + len(txt)]
  for i in range(len(y)):
    if y == txt:
      return 'No Missing Letter'
    elif y[i] == txt[i]:
      continue
    else:
      return y[i]

