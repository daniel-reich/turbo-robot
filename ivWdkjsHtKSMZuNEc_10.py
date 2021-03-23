"""


Create a function that accepts a string as an argument. Find its shortest
word(s) and return them as a list sorted alphabetically (if there are multiple
shortest words).

### Examples

    find_shortest_words("I think the solution is fairly obvious.") ➞ ["i"]
    
    find_shortest_words("Chase two rabbits, catch none.") ➞ ["two"]
    
    find_shortest_words("We become what we think about.") ➞ ["we", "we"]
    
    find_shortest_words("The quick brown fox jumped over the lazy dogs back.") ➞ ["fox", "the", "the"]

### Notes

  * Periods, commas and other special characters don't count as part of a word's length.
  * Remember to sort the list of words alphabetically before returning your result.
  * Return words in lowercase only.

"""

import re
​
def find_shortest_words(txt):
  print(txt.split())
  words = txt.split()
  words_letters = []
  shortest_word_length = 100
  short_words =[]
  
  for word in words:
    words_letters.append(re.sub('[^a-zA-Z]', '', word).lower())
  words_letters = list(filter(None, words_letters))
  print(words_letters)
  
  for word in words_letters:
    print(word, len(word))
    if len(word) < shortest_word_length:
      shortest_word_length = len(word)
      short_words = [word]
    elif len(word) == shortest_word_length:
      short_words.append(word)
  print(sorted(short_words))
  return sorted(short_words)

