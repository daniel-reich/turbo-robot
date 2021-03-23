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
    ans = "An " if words[0][0] in "aeiou" else "A "
    ans += words.pop(0)
    for word in words[:-1]:
        if word[0] in "aeiou":
            ans += ", an " + word
        else:
            ans += ", a " + word
    ans += " and "
    if words[-1][0] in "aeiou":
        ans += "an " + words[-1]
    else:
        ans += "a " + words[-1]
    return ans + "."

