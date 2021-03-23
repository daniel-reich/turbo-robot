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
  vowels=['a','e','i','o','u']
  upper=False
  if len(word)==0:
    return word
  else:
    if word[0].isalpha() and word[0].lower() in vowels:
      word+='yay'
    else:
      word1=''
      for i in range (0,len(word)):
        if not (word[i].lower() in vowels):
          if (i==0 and word[i].upper()==word[i]):
            upper=True
          word1+=word[i].lower()
        else:
          if upper:
            word=word[i].upper()+word[min(i+1,len(word)):]+word1 +'ay'
          else:
            word=word[i:]+word1 +'ay'
          break
    return word 
​
def translate_sentence(sentence):
  out, i='',0
  lst=re.findall(r"[A-Za-z@#]+|.", sentence)
  for i in range (len(lst)):
    if(lst[i].isalpha()):
      out+=translate_word(lst[i])
    else:
      out+=lst[i]
  return out

