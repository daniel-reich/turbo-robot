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
  if words == None:
    return ""
  elif (len(words) == 0 or words[0] == ""):
    return ""
  elif len(words) == 1:
    return words[0]
  else:
    if "" in words:
      words.remove("")
    temp = ", ".join([words[i] for i in range(len(words)-1)])
    return temp + " and " + words[-1]

