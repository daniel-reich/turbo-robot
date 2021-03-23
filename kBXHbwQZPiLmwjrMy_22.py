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
    vowels = 'aeiou'
    vowelind = []
    for tchar in vowels:
        ind = word.lower().find(tchar)
        if ind>-1:
            vowelind.append(ind)
    if len(vowelind)==0:
        return word
    fwi = min(vowelind) #first vowel index
    if fwi == 0:
        anotherword = word+"yay"
    else:
        anotherword = word[fwi:]+word[0:fwi]+"ay"
    anotherword = anotherword.lower()
    if word[0].isupper():
        anotherword=anotherword[0].upper()+anotherword[1:]
    return anotherword
​
​
​
​
def translate_sentence(sentence):
    translated = ""
    words = re.split('(\W+)', sentence)
    for w in words:
        if w.isalpha():
            translated += translate_word(w) 
        else:
            translated += w
    return translated

