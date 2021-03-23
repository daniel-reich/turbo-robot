"""


Pig latin has two very simple rules:

  1. If a word starts with a consonant move the first letter(s) of the word, till you reach a vowel, to the end of the word and add "ay" to the end.
    * have ➞ avehay
    * cram ➞ amcray
    * take ➞ aketay
    * cat ➞ atcay
    * shrimp ➞ impshray
    * trebuchet ➞ ebuchettray
  2. If a word starts with a vowel add "yay" to the end of the word.
    * ate ➞ ateyay
    * apple ➞ appleyay
    * oaken ➞ oakenyay
    * eagle ➞ eagleyay

Write two functions to make an English to pig latin translator. The first
function `translate_word(word)` takes a single word and returns that word
translated into pig latin. The second function `translate_sentence(sentence)`
takes an English sentence and returns that sentence translated into pig latin.

### Examples

    translate_word("flag") ➞ "agflay"
    
    translate_word("Apple") ➞ "Appleyay"
    
    translate_word("button") ➞ "uttonbay"
    
    translate_word("") ➞ ""
    
    translate_sentence("I like to eat honey waffles.") ➞ "Iyay ikelay otay eatyay oneyhay afflesway."
    
    translate_sentence("Do you think it is going to rain today?") ➞ "Oday ouyay inkthay ityay isyay oinggay otay ainray odaytay?"

### Notes

  * Regular expressions will help you not mess up the punctuation in the sentence.
  * If the original word or sentence starts with a capital letter, the translation should preserve its case (see examples #2, #5 and #6).

"""

import re
​
​
def translate_word(word):
  if len(word) == 0:
    return ''
  word_indexes = [(m.start(0), m.end(0)) for m in re.finditer('[a-zA-Z]', word)]
  translatable_word = word[min(word_indexes)[0] : max(word_indexes)[1]]
  is_capitalized = translatable_word[0].isupper()
  translatable_word = translatable_word.lower().lstrip().rstrip()
  index = get_index(translatable_word)
  if index == 0:
    translatable_word = translatable_word + 'yay'
  else:
    translatable_word = translatable_word[index:] + translatable_word[:index] + 'ay' 
  
  if is_capitalized:
    translatable_word = translatable_word.capitalize()
  return word.replace(word[min(word_indexes)[0] : max(word_indexes)[1]], translatable_word)
​
def translate_sentence(sentence):
  str = []
  for index,word in enumerate(sentence.split()):
    str.append(translate_word(word))
  return " ".join(str)
​
def get_index(word):
  for index,value in enumerate(word):
    if value.lower() in 'aeiou':
      return index
      break

