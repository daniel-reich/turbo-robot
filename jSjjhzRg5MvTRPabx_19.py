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

def sentence(nouns):
    nouns = [
    "an " + noun if noun[0] in "aeiou" else "a " + noun 
    for noun in nouns
  ]
    nouns[-1] = "and " + nouns[-1] + "."
    nouns[0] = nouns[0][1:]
    return "A" + ", ".join(nouns[:-1]) + " " + nouns[-1]

