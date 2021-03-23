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

vowels = "aeiouAEIOU"
letters = [chr(k) for k in range(65, 91)] + [chr(k) for k in range(97, 123)]
​
def translate_word(word):
    if len(word) == 0:
        return word
    first_upper = 'A' <= word[0] <= 'Z'
    if word[0] not in vowels:
        while word[0] not in vowels:
            word = word[1:] + word[0].lower()
        word += "ay"
        if first_upper:
            word = word[0].upper() + word[1:]
    else:
        word += "yay"
    return word
  
​
def translate_sentence(sentence):
    if sentence == "":
        return ""
    txt = sentence
    pig = ""
    word = ""
    for char in txt:
        if char in letters:
            word += char
        else:
            pig += translate_word(word)
            word = ""
            pig += char
    if word != "":
        pig += translate_word(word)
    pig = pig[0].upper() + pig[1:]
    return pig

