"""


Create a function that turns a list of words into a comma separated list,
where the last word is separated by the word "and".

### Examples

    words_to_sentence(["edabit"]) ➞ "edabit"
    
    words_to_sentence(["Hello", "", "Bye"]) ➞ "Hello and Bye"
    
    words_to_sentence(["Hello", "Bye", "See you soon"]) ➞ "Hello, Bye and See you soon"

### Notes

`None` values, empty lists or lists with only empty or `None` values should
return an empty string: `""`

"""

def words_to_sentence(words):
  if words == None: return ""
  if "" in words: words.remove("")
  if len(words) == 1: return ''.join(words)
  return ("" if len(words) < 1 else str(', '.join(words[:-1]) + ' and ' + words[-1]))

