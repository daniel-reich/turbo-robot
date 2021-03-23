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
def translate_word(word):
    if not word:
        return ''
    vowels = 'aeiou'
    capitalized = True if word[0].isupper() else False
    if word[0].lower() in vowels:
        return word + 'yay'
    else:
        i = 1
        while i < len(word) and word[i] not in vowels:
            i += 1
        return (word[i:] + word[:i] + 'ay').capitalize() \
            if capitalized else word[i:] + word[:i] + 'ay'
​
​
def translate_sentence(sentence):
    if not sentence:
        return ''
    lst = sentence.split()
    for i in range(len(lst)):
        begin_word, end_word = -1, len(lst[i])
        for j in range(len(lst[i])):
            if lst[i][j].isalpha():
                if begin_word == -1:
                    begin_word = j
            else:
                if begin_word != -1 and end_word == len(lst[i]):
                    end_word = j
        lst[i] = lst[i][:begin_word] \
            + translate_word(lst[i][begin_word: end_word]) \
            + lst[i][end_word:]
    return ' '.join(lst)

