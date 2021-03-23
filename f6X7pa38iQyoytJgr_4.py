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
  def weight_finder(word):
    l = list(word)
    exclude = '/ ! , . ? \" \' @ : ; # ~'.split() #It is important to remove any punctuation as this throws off the calcuations!
    
    codes = []
    
    for l8r in l:
      if l8r not in exclude:
        code = ord(l8r)
        codes.append(code)
    
    s = sum(codes)
    
    return s
  
  word_weights = {}
  values = []
  
  sentence = sentence.split()
  
  for word in sentence:
    
    value = weight_finder(word)
    
    if value not in word_weights:
      word_weights[value] = [word]
    else:
      word_weights[value].append(word)
    
    if value not in values:
      values.append(value)
  
  values = sorted(values)
  
  sorted_words = []
  
  for value in values:
    words = word_weights[value]
    for word in words:
      sorted_words.append(word)
  
  if sorted_words == sentence:
    return True
  else:
    return False

