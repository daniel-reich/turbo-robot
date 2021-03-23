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
  if not words or not words[0]: return ''
  if len(words) == 1: return words[0]
  
  words = [x for x in words if x]
  words[-1] = 'and ' + words[-1]
  words = [x + ',' for x in words[:-2]] + words[-2:]
  return ' '.join(words)

