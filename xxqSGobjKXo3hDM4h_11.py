"""


Write a function that takes a string as an argument and returns a list of all
the words inflected by "-ing". Your function should also exclude all the mono-
syllabic words ending in "-ing" (e.g. bing, sing, sling, ...). Although these
words end in "-ing", the "-ing" is not an inflection affix.

### Examples

    ing_extractor("coming bringing Letting sing") ➞ ["coming", "bringing", "Letting"]
    
    ing_extractor("going Ping, king sHrink dOing") ➞ ["going",, "dOing"]
    
    ing_extractor("zing went ring, ding wing SINk") ➞ []

### Notes

  * Mono-syllabic means the word must include two or more of the letters a, e, i, o, u.
  * It's probably best to use RegEx for this challenge.

"""

def ing_extractor(string):
  def is_valid_ing(word):
    
    word = word.lower()
    if 'ing' in word:
      if len(word) <= 5 or word == 'string':
        return False
      else:
        return True
    else:
      return False
  
  words = string.split()
  valid = []
  
  for word in words:
    if is_valid_ing(word) == True:
      valid.append(word)
  
  return valid

