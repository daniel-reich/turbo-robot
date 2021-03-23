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

VOWELS = 'aeiou'
PUNCTUATION = '!.,?:;"'
​
def translate_word(word):
    '''
    Returns word translated to pig latin as per the instructions
    '''
    if not word:
        return ''
​
    size = len(word)
    if word[0] in PUNCTUATION:
        i = 1
        start_punc = 1
    else:
        i = 0
        start_punc = 0  # adjust for leading punctuation
        
    end_punc = size
    for j in range(1, size):
        if word[j] in PUNCTUATION:
            end_punc = j   # where trailing punctuation starts
            break
    
    pig = 'yay' if word[i].lower() in VOWELS else 'ay'
    capital = True if word[i].isupper() else False
    while not word[i].lower() in VOWELS:
        i += 1
        
    if capital:
        word = word[:i].lower() + word[i].upper() + word[i+1:].lower()
​
    return word[0:start_punc] + word[i:end_punc] + word[start_punc:i] + pig + word[end_punc:]
    
def translate_sentence(sentence):
    '''
    Translates sentence into pig latin as per the instructions
    '''
    return ' '.join([translate_word(word) for word in sentence.split()])

