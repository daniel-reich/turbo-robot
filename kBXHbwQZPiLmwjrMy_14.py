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
from string import ascii_uppercase
​
def translate_word(word):
  if word == "":
    return word
  upper = False
  if re.search(r"\b(\w)", word).group(1) in ascii_uppercase:
    upper = True
    word = word.lower()
​
  rv = ""
  if re.search(r"\b([aeiou])+.*", word) is not None:
    rv = re.sub(
      r"(\W*)([aeiou]+)(\w*)(\W*)",
      r"\1\2\3yay\4",
      word
      )
  else:
    rv = re.sub(
      r"(\W*)([^aeiou]+)([aeiou]+\w*)(.*)",
      r"\1\3\2ay\4",
      word
      )
  
  if upper:
    for i, c in enumerate(rv):
      if c.isalpha():
        break
    return rv[:i] + rv[i:].capitalize() 
  else:
    return rv
​
def translate_sentence(sentence):
  if len(sentence) < 1:
    return sentence
  new_sentence = ""
  for word in sentence.split(" "):
    new_sentence += translate_word(word) + " "
    
  return new_sentence.strip()

