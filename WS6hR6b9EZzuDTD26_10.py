"""


Given a common phrase, return `False` if _any_ individual word in the phrase
contains _duplicate_ letters. Return `True` otherwise.

### Examples

    no_duplicate_letters("Fortune favours the bold.") ➞ True
    
    no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True
    
    no_duplicate_letters("Look before you leap.") ➞ False
    # Duplicate letters in "Look" and "before".
    
    no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
    # Duplicate letters in "apple", "keeps", "doctor", and "away".

### Notes

Letter matches are case-insensitive.

"""

from collections import Counter
def no_duplicate_letters(phrase):
  lst = phrase.split(" ")
  
  for word in lst:
    a = Counter([char for char in word])
    for key in list(a.keys()):
      if a[key] > 1:
        return False
  
  return True

