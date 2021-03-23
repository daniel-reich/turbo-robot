"""


Write a function that splits a string into substrings of size n, adding a
specified delimiter between each of the pieces.

### Examples

    split_and_delimit("bellow", 2, "&") ➞ "be&ll&ow"
    
    split_and_delimit("magnify", 3, ":") ➞ "mag:nif:y"
    
    split_and_delimit("poisonous", 2, "~") ➞ "po~is~on~ou~s"

### Notes

N/A

"""

def split_and_delimit(txt, num, delimiter):
  result = ""
  counter = 0
  for c in txt:
    if counter == num:
      result += delimiter
      counter = 0
    result += c
    counter += 1
  
  return result

