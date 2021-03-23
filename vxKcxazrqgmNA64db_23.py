"""


A word has been split into a `left` part and a `right` part. Re-form the word
by adding both halves together, changing the _first_ character to an uppercase
letter.

### Examples

    get_word("seas", "onal") ➞ "Seasonal"
    
    get_word("comp", "lete") ➞ "Complete"
    
    get_word("lang", "uage") ➞ "Language"

### Notes

N/A

"""

def get_word(left, right):
    new_word = left.title() + right
    return new_word
​
​
print(get_word("seas", "onal"))
print(get_word("comp", "lete"))
print(get_word("lang", "uage"))

