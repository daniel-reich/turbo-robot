"""


Create a function that takes a string and returns the reversed string. However
there's a few rules to follow in order to make the challenge interesting:

  * The UPPERCASE/lowercase positions must be kept in the same order as the original string (see example #1 and #2).
  * Spaces must be kept in the same order as the original string (see example #3).

### Examples

    special_reverse_string("Edabit") ➞ "Tibade"
    
    special_reverse_string("UPPER lower") ➞ "REWOL reppu"
    
    special_reverse_string("1 23 456") ➞ "6 54 321"

### Notes

N/A

"""

def special_reverse_string(txt):
  list_str = list(txt)
  list_str.reverse()
  list_str = list(filter( lambda x: x!=" ", list_str))
  print(list_str)
  reverse = []
  for char in txt:
    if char == " ":
      reverse.append(" ")
    elif char.isupper():
      reverse.append(list_str.pop(0).upper())
    else:
      reverse.append(list_str.pop(0).lower())
  string =""
  return string.join(reverse)

