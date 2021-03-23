"""


For this challenge, the input will be a (long) string.

A word encountered for the first time is a stranger. A word encountered thrice
becomes an acquaintance. A word encountered 5 times becomes a friend.

Create a function that takes the string and returns a list of two lists. The
first is a list of acquaintances in the order they became an acquaintance (see
example). The second is a list of friends in the order they became a friend.
Words on the friend list should no longer be on the acquaintance list.

### Examples

    no_strangers("See Spot run. See Spot jump. Spot likes jumping. See Spot fly.")
    ➞ [["spot", "see"], []]
    # "see" was encountered first, but "spot" became an acquaintance earlier.

### Notes

  * All words should be in lowercase.
  * Punctuation should be stripped except for apostrophes (e.g. doesn't, aren't, etc).

"""

def indexes(sentence, word):  
  indexes = []
  no_punct = ''
  for char in sentence:
    if char in '.",!':
      no_punct += ''
    else:
      no_punct += char.lower()
  word_list = no_punct.split(' ')
  for i in range(len(word_list)):
    if word_list[i] == word.lower():
      indexes.append(i)
  return indexes
    
​
​
def no_strangers(sentence):
  no_punct = ''
  for char in sentence:
    if char in '.",!':
      no_punct += ''
    else:
      no_punct += char.lower()
  word_list = no_punct.split(' ')
  acquaintance = []
  friend = []
  for word in word_list:
    if word_list.count(word) == 3 or word_list.count(word) == 4:
      if acquaintance.count(word) == 0:
        acquaintance.append(word)            
    elif word_list.count(word) >= 5:
      if friend.count(word) == 0:
        friend.append(word)
  return [sorted(acquaintance, key = lambda word: indexes(sentence, word)[2]), 
            sorted(friend, key = lambda word: indexes(sentence, word)[4])]

