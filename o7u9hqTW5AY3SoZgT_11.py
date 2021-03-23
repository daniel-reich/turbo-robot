"""


Create a function which **replaces** all instances of `"nts"` with `"nce"` and
**vice versa** if they are at the _end of a word_.

### Examples

    switcheroo("The elephants in France were chased by ants!") ➞ "The elephance in Frants were chased by ance!"
    
    switcheroo("While he rants, I fall into a trance...") ➞ "While he rance, I fall into a trants..."
    
    switcheroo("Bounced over the fence!") ➞ "Bounced over the fents!"

### Notes

  * Empty strings should return just an empty string (see example #2).
  * Ignore punctuation and any instances where `"nts"` or `"nce"` are not at the end of a word (see example #3).

"""

def w_replace(word):
  new_word = word.replace('.','') \
    .replace(',','') \
    .replace("'",'')\
    .replace('!','')
    
  if new_word.endswith('nts'):
    return new_word.replace('nts','nce') + word[word.index('nts')+3:]
  elif new_word.endswith('nce'):
    return new_word.replace('nce', 'nts') + word[word.index('nce')+3:]
  else:
    return word
​
def switcheroo(txt):
  return ' '.join(map(w_replace, [w for w in txt.split()]))

