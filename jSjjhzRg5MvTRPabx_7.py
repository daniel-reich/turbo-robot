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

def sentence(words):
  newlist = []
  newlist2 = []
  for i in range(len(words)):
    if i+1 == len(words)-1:
      x = starts_with_vowel(words[i])
      y = starts_with_vowel(words[i+1])
      newlist2.append(x)
      newlist2.append(y)
      z = ' and '.join(newlist2)
      newlist.append(z)
      break
    else:
      newlist.append(starts_with_vowel(words[i]))
  return '{}.'.format(', '.join(newlist).capitalize())
​
def starts_with_vowel(word):
  newlist = []
  vowels = 'aeiouAEIOU'
  if word[0] in vowels:
    newlist.append('an')
    newlist.append(word)
  else:
    newlist.append('a')
    newlist.append(word)
  return ' '.join(newlist)

