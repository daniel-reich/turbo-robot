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
    v = ['a','e','i','o','u']
    for i in range(len(words)):
        if words[i][0] in v:
            if i < len(words)-2:
                words[i] = 'an ' + words[i] + ','
            else:
                words[i] = 'an ' + words[i]
        else:
            if i < len(words)-2:
                words[i] = 'a ' + words[i] + ','
            else:
                words[i] = 'a ' + words[i]
    words[0] = words[0].capitalize()
​
    words[-1] = 'and ' + words[-1] + '.'
​
    return ' '.join(words)

