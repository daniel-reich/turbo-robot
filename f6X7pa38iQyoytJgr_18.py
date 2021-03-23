"""


The _weight_ of an English word can be calculated by summing the `ASCII` code
point for each character in the word, _excluding_ any punctuation:

    "Wouldn't" = 87 + 111 + 117 + 108 + 100 + 110 + 116 = 749

Write a function that takes a sentence as a string, returning `True` if all
word weights increase for each word in the sentence, and `False` if any word
weight decreases or remains the same.

### Examples

    increasing_word_weights("Why not try?") ➞ True
    # 312 -> 337 -> 351 (weights increase)
    
    increasing_word_weights("All other roads.") ➞ False
    # 281 -> 546 -> 537 (537 is less than 546)

### Notes

Check the **Resources** for links on how to return character codes.

"""

def increasing_word_weights(sentence):
  wds = sentence.split()
  weights = []
  for w in wds:
    weight = 0
    for ch in w:
      if ch.isalpha():
        weight += ord(ch)
    weights.append(weight)
  for i in range(len(weights)-1):
    if weights[i] >= weights[i+1]:
      return False
  return True

