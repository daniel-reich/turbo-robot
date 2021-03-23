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
  end=" and an "+words[-1] if words[-1][0] in "aeiou" else " and a "+words[-1]
  return ", ".join("an "+word if word[0] in "aeiou" else "a "+word for word in words[:-1]).capitalize()+end+"."

