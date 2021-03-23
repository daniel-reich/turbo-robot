"""


Write a function that replaces all letters within a specified range with the
hash symbol `#`.

### Examples

    replace("abcdef", "c-e") ➞ "ab###f"
    
    replace("rattle", "r-z") ➞ "#a##le"
    
    replace("microscopic", "i-i") ➞ "m#croscop#c"
    
    replace("", "a-z") ➞ ""

### Notes

  * The range will always be in order, a.k.a. for `m-n`, character `m` will always come before or equal `n`.
  * Strings will be in lower case letters only.
  * Return an empty string if the input is an empty string.

"""

def replace(txt, r):
  if (not txt):
    return txt
  alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
              "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", 
              "u", "v", "w", "x", "y", "z"]
  limits = r.split("-")
  initial_index = alphabet.index(limits[0])
  final_index = alphabet.index(limits[1])
  in_limits = [alphabet[i] for i in range(initial_index,final_index+1)]
  hashed_word = ""
  for letter in txt:
    if (letter in in_limits):
      hashed_word += "#"
    else:
      hashed_word += letter
  return hashed_word

