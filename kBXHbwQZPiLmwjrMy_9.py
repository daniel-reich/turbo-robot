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
def translate_word(word: str):
  vowels = re.findall(r'[aeuioAEUIO]', word)
  try:
    idx = word.index(vowels[0])
    if idx > 0:
      ret_word = word[idx:] + word[:idx] + 'ay'
    else:
      ret_word = word + 'yay'
​
  except IndexError:
    return ''
​
  if word[0].isupper():
    return (ret_word.lower()).capitalize()
  else:
    return ret_word
​
​
​
​
def translate_sentence(sentence):
  words = sentence.split()
​
  punctuation_before = [re.findall(r'([^\w]+)[\w]', word) for word in words]
  punctuation_after = [re.findall(r'[\w]([^\w]+)', word) for word in words]
​
  words = [re.sub(r'[:.,"?!\'/_\\()<>{}\[\];-]*(\w+)[:.,"?!\'/_\\()<>{}\[\];-]*', r'\1', word) for word in words]
  words = [translate_word(word) for word in words]
​
  ret_words = []
​
  for word, punct_before, punct_after in zip(words, punctuation_before, punctuation_after):
    if punct_after and punct_before:
      ret_words.append(punct_before[0] + word + punct_after[0])
​
    elif punct_before:
      ret_words.append(punct_before[0] + word)
​
    elif punct_after:
      ret_words.append(word + punct_after[0])
​
    else:
      ret_words.append(word)
​
  return ' '.join(ret_words)

