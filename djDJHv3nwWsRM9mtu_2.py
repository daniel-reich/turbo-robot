"""


Given a sentence spelling out a word, return `True` if the spelled letters
match the _word at the end of the string_.

### Examples

    validate_spelling("C. Y. T. O. P. L. A. S. M. Cytoplasm?") ➞ True
    
    validate_spelling("P. H. A. R. A. O. H. Pharaoh!") ➞ True
    
    validate_spelling("H. A. N. K. E. R. C. H. E. I. F. Handkerchief.") ➞ False

### Notes

  * The word at the end is **always spelled correctly**.
  * Spelled words will always end in punctuation (but ignore all punctuation).

"""

import re
​
letter_regex = re.compile(r'\b(\w)\.')
word_regex = re.compile(r'(\w+)[!.?]$')
​
​
def validate_spelling(txt):
    letters = (''.join(letter_regex.findall(txt)))
    words = (''.join(word_regex.findall(txt)))
    if letters.lower() == words.lower():
        return True
    return False

