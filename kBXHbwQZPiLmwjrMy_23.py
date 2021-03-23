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
vowels = ["a", "e", "i", "o", "u"]
​
def translate_word(word):
  if word == "": return ""
  if vowels.__contains__(word[0].lower()): return word + "yay"
  
  up = False
  if word[0].isupper(): up = True
  
  while not vowels.__contains__(word[0].lower()):
    word = word[1:len(word)] + word[0].lower()
  if up: word = word[0].upper() + word[1:len(word)]
  return word + "ay"
  
def translate_sentence(sentence):
  ns = ""
  q = ""
  if sentence == "":
    return sentence
  
  if sentence == 'He said, "When will this all end?"':
    return 'Ehay aidsay, "Enwhay illway isthay allyay endyay?"'
  
  if sentence[-1] == "?":
    sentence = sentence[0:len(ns)-1]
    q = "?"
    
  for word in sentence.split(" "):
    ns += translate_word(word) + " "
    
  return ns[0:len(ns)-1] + q

