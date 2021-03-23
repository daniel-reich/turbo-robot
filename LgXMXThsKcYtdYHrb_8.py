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
  new = ""
  for x in range(len(txt) // num):
    new += txt[x * num: x * num + num] + delimiter
  if len(txt) // num != len(txt) / num:
    new += txt[len(txt) // num * num:]
  if new[-1] == delimiter:
    new = new[:-1]
  return new

