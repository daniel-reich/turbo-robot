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

def common_last_vowel(txt):
    ll = []
    for i in txt:
        if i[-1] in "aeiouAEIOU":
            ll.append(i.lower())
    return (ll)[-1]

