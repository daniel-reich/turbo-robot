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
    vow = 'aeiou'
​
    def vv(s):
        if s[0] in vow:
            return 'an ' + s
        else:
            return 'a ' + s
​
    buf = [vv(x) for x in words]
    muf = [vv(x) for x in words][0:-1]
    return ', '.join(muf).capitalize() + ' and ' + buf[-1] + '.'

