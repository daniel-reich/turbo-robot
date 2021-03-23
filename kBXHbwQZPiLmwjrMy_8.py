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
def translate_word(word):
  if (word == ""):
    return word
  vowel = False
  if (re.match("^[aeiouAEIOU]", word)):
    vowel = True
  if (vowel):
    return word+"yay"
  consonant = re.search("^[^aeiouAEIOU]+", word).group()
  clen = len(consonant)
  new_word = word[clen:]
  if (consonant[0].isupper()):
    new_word = list(new_word)
    new_word[0] = new_word[0].upper()
    new_word = "".join(new_word)
  consonant = consonant.lower()
  new_word += consonant+"ay"
  return new_word
​
def translate_sentence(sent):
  if (sent == ""):
    return sent
  sent += " "
  word_pat = r"\w+"
  not_word_pat = r"\W+"
  words = re.findall(word_pat, sent)
  not_words = re.findall(not_word_pat, sent)
  for i, c in enumerate(words):
    words[i] = translate_word(c)
  return "".join([words[i]+not_words[i] for i, c in enumerate(words)]).rstrip()

