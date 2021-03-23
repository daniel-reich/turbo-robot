"""


Write a function that retrieves all words that begin with a vowel.

### Examples

    retrieve("A simple life is a happy life for me.") ➞ ["a", "is", "a"]
    
    retrieve("Exercising is a healthy way to burn off energy.")
    ➞ ["exercising", "is", "a", "off", "energy"]
    
    retrieve("The poor ostrich was ostracized.")
    ➞ ["ostrich", "ostracized"]
    
    retrieve("")
    ➞ []

### Notes

  * Make all words lower case in the output.
  * Retrieve the words in the order they appear in the sentence.

"""

import re
def retrieve(txt):
  txt = txt.strip('.')
  txt = txt.split()
  pattern = r'[aeiou]'
  res_lst = []
  for word in txt:
    if re.match(pattern, word, re.I):
      res_lst.append(word.lower())
  return res_lst

