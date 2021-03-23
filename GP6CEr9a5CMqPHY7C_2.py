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
  try:
    words = [i for i in words if i != None or i if i != '']
    part1 = words[0:-1] + ['and'] + words[-1:]
    if len(words) == 2:
      return ' '.join(part1)
    if len(words) == 1:
      return words[0]
    if len(words) == 0:
      return ''
    return ', '.join(part1[0:-3])+ ', ' + ' '.join(part1[-3:])
  except:
      return ''

