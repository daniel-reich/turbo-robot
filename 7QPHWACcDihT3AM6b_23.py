"""


You are given an input array of bigrams, and an array of words.

Write a function that returns `True` if **every single bigram** from this
array can be found at least **once** in an array of words.

### Examples

    can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]) ➞ True
    
    can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]) ➞ False
    # "cu" does not exist in any of the words.
    
    can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) ➞ True
    
    can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]) ➞ False

### Notes

  * A **bigram** is string of two consecutive characters in the same word.
  * If the list of words is empty, return `False`.

"""

def can_find(bigrams, words):
  count = 0
  for chars in bigrams:
    for word in words:
      if chars in word:
        count += 1
    if count == 0:
      return False
    count = 0
  return True

