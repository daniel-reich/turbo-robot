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
  else:
    output = ""
    realwords = [k for k in words if k != None and k != ""]
    for i in range(len(realwords)):
      if realwords[i] != None and realwords[i] != "":
        if i < len(realwords) - 2:
          output = output + realwords[i] + ", "
        elif i == len(realwords) - 2:
          output = output + realwords[i] + " and "
        elif i == len(realwords) - 1:
          output = output + realwords[i]
​
    return output

