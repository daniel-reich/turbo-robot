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
  newlist = []
  newlist2 = []
  if type(words) == type(None):
    return ''
  elif len(words) == 1:
    return words[0]
  elif len(words) == 0:
    return ''
  else:
    for eachword in words:
      if eachword == '':
        continue
      else:
        newlist2.append(eachword)
    x = ' '.join(newlist2)
    lasttwo = newlist2[-2:]
    lasttwo = ' and '.join(lasttwo)
    lasttwo = (lasttwo.lstrip(' ')).rstrip(' ')
    therest = newlist2[:-2]
    for eachword in therest:
      newlist.append(eachword + ',')
    x = ' '.join(newlist)
    return (('{} {}'.format(x,lasttwo)).lstrip(' ')).rstrip(' ')

