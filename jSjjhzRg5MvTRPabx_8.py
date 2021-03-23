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
  if words[0][0] in 'aeiou':
    ret = 'An '+words[0]
  else:
    ret = 'A '+words[0]
  for i in range(1,len(words)-1):
    if words[i][0] in 'aeiou':
      ret+=', an '+words[i]
    else:
      ret+=', a '+words[i]
  if words[-1][0] in 'aeiou':
    ret+=' and an '+words[-1]+'.'
  else:
    ret+=' and a '+words[-1]+'.'
  return ret

