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

def translate_word(s):
    vows = 'aoueiAOUEI'
    if not s:
        return s
    if s[0] in vows:
        return s + "yay"
    for i in range(1, len(s)):
        if s[i] in vows:
            if s[0].isupper():
                return s[i].upper() + s[i+1:] + s[0].lower() + s[1:i] + 'ay'
            else:
                return s[i:] + s[:i] + 'ay'
​
​
def translate_sentence(s):
    ws = []
    for w in s.split():
        i, j = 0, len(w)-1
        while i < len(w) and not w[i].isalpha():
            i += 1
        while j > i and not w[j].isalpha():
            j -= 1
        w_strip = w[i:j+1]
        ws.append(w[:i] + translate_word(w_strip) + w[j+1:])
    return ' '.join(ws)

