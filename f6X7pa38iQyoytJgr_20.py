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

sentence01 = "it's a hard knock life"
sentence02 = "a big booty woman"
​
def increasing_word_weights(sentence):
  # compare integer value of each word in a list and returns True if each is greater than the previous
  lst = word_weights(sentence)
  mx = lst[0]
  for i in lst:
    if i > mx:
      mx = i
    elif i < mx:
      break
  return True if [mx] == lst[-1:] else False
​
def word_weights(sentence):
  # Get the value of each character in each word and add them per word.
  words = convert_to_list(sentence)
  ords = []
  word_values = []
  character_value = 0
  word_value = 0
  for i in range(len(words)):
    ords.append(character_value)
    
    for character in words[i]:
      if character.isalpha():
        character_value += ord(character)
    word_value = character_value - ords[i]
    word_values.append(word_value)
  return word_values
​
def convert_to_list(sentence):
  # changes sentence to list, to separate words
  return (sentence.split())

