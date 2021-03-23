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
from string import punctuation
​
def translate_word(word):
    list_word = list(word)
    if list_word == []: return ''
    letters = [char.lower() for char in list_word if char not in punctuation]
    if letters[0] not in 'aeiouAEIOU':
        while letters[0] not in 'aeiouAEIOU':
            letters.append(letters.pop(0))
        letters.append('ay')
    else: letters.append('yay')
    for count,char in enumerate(list_word):
        if char in punctuation and count == 0:
            letters.insert(0,char)
        elif char in punctuation:
            letters.append(char)
    for index in [list_word.index(x) for x in list_word if x.isupper()]:
        letters[index] = letters[index].upper()
    return ''.join(letters)
​
def translate_sentence(sentence):
  return ' '.join([translate_word(word) for word in sentence.split()])

