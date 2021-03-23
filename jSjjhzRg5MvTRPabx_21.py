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
    ans =''
    for i, w in enumerate(words):
        if w[0] in 'aeiou':
            pre = 'an '
        else:
            pre = 'a '
        if i == len(words) - 1:
            beg = ' and '
        elif i == 0:
            beg = ''
        else:
            beg = ', '
        ans += beg + pre + w
    ans += '.'
    return ans.capitalize()

