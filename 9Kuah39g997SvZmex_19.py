"""


Create a function that takes in a sentence as input and returns the **most
common last vowel** in the sentence as a single character string.

### Examples

    common_last_vowel("Hello World!") ➞ "o"
    
    common_last_vowel("Watch the characters dance!") ➞ "e"
    
    common_last_vowel("OOI UUI EEI AAI") ➞ "i"

### Notes

  * There will only be one common last vowel in each sentence.
  * If the word has one vowel, treat the vowel as the last one **even if it is at the start of the word**.
  * The question asks you to compile all of the last vowels of each word and returns the vowel in the list which appears most often.
  *  **y** won't count as a vowel.
  * Return outputs in **lowercase**.

"""

import re
​
​
​
def common_last_vowel(txt):
    vowels = "aeiouAEIOU"
    counts = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }
    for word in txt.split():
        word = ''.join([letter for letter in word if letter.isalpha()])
        if word[-1] in vowels:
            counts[word[-1].lower()] += 1
        else:
            matches = re.findall(r"[aeiouAEIOU]", word)
            if len(matches) == 1:
                counts[matches[0].lower()] += 1
    return max([(letter, total) for letter, total in counts.items()], key=lambda x: x[1])[0]

