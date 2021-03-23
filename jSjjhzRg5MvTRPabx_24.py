"""


Given a list of strings (nouns), list them up in a complete sentence.

### Examples

    sentence(["orange", "apple", "pear"]) ➞ "An orange, an apple and a pear."
    
    sentence(["keyboard", "mouse"]) ➞ "A keyboard and a mouse."
    
    sentence(["car", "plane", "truck", "boat"]) ➞ "A car, a plane, a truck and a boat."

### Notes

  * The sentence starts with a **capital letter**.
  * Do not change **the order** of the words.
  *  **A/An** should be correct in all places.
  * Put commas between nouns, except between the last two (there you put "and").
  * The sentence ends with a `.`
  * There are at least two nouns given.
  * Every given word is lowercase.

"""

import re
def sentence(word):
  result = ''
  lst = ["an " + i if bool(re.match(r"[aeiou]", i)) else "a " + i for i in word]
  for i in range(len(word)):
    item = lst[i]
    if i == len(word) - 2:
       result += item + " and "
    elif i == len(word) - 1:
       result += item + "."
    else:
       result += item + ", "
  return result[0].upper() + result[1:]

