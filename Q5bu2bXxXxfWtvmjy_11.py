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

alphabet = 'abcdefghijklmnopqrstuvwxyz'
​
def missing_letter(txt):
  output = []
  for i in alphabet:
    if i > txt[0] and i < txt[-1] and i not in txt:
      output.append(i)
  if len(output) == 0:
    return "No Missing Letter"
  return output[0]

