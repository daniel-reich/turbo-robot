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

def last_vowel(word):
  for i in word[::-1]:
    if i.lower() in 'aeiou':
      return i.lower()
​
def common_last_vowel(txt):
  words = txt.split(' ')
  last = {}
  for word in words:
    lv = last_vowel(word)
    if lv not in last:
      last[lv] = 1
    else:
      last[lv] += 1
  counts = [last[i] for i in last]
  winner = [i for i in last if last[i] == max(counts)]
  return winner[0]

