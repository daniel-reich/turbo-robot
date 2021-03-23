"""


Write a function that stutters a word as if someone is struggling to read it.
The first two letters are repeated twice with an ellipsis `...` and space
after each, and then the word is pronounced with a question mark `?`.

### Examples

    stutter("incredible") ➞ "in... in... incredible?"
    
    stutter("enthusiastic") ➞ "en... en... enthusiastic?"
    
    stutter("outstanding") ➞ "ou... ou... outstanding?"

### Notes

Assume all input is in lower case and at least two characters long.

"""

def stutter(word):
  short_word = ""
  for i in range(2):
    short_word += (word[i])
  stutter_string = short_word + "... " + short_word + "... "
  full_string = stutter_string + word + "?"
  return full_string

