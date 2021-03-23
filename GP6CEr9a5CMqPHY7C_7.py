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
  a = ""
  i = 0
  c = []
  if words == None or len(words) == 0:
    return ""
  elif len(words) == 1:
    return words[0]
  for index in words:
    if index != "":
      c.append(index)
  while i < len(c)-1:
    a += c[i]
    if i == len(c) -2 : 
      break
    a += ", "
    i += 1
  a = a + " and " + c[i+1]  
  return a

