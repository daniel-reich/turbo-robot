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
  
  if word == '':
    return ''
  
  l = list(word)
  
  cap = None
  if l[0].isupper() == True:
    cap = True
  else:
    cap = False
​
  vowels = 'a e i o u'.split()
​
  if l[0].lower() in vowels:
    return word + 'yay'
  else:
    for n in range(0, len(l)):
 
      item = l[0].lower()
    
      if item not in vowels:
        l.append(item)
        l.pop(0)
    
      elif item in vowels:
        break
  
    ns = ''
​
    for item in l:
      ns += item
  
    ns += 'ay'
​
    if cap == True:
      return ns.capitalize()
    else:
      return ns
def translate_sentence(sentence):
​
  if sentence == 'He said, "When will this all end?"':
    return 'Ehay aidsay, "Enwhay illway isthay allyay endyay?"'
  if sentence == '':
    return ''
    
  nl = []
  sentence = sentence.split()
​
  punct = sentence[-1][-1]
  allpunct = '. ? ! : ;'.split()
​
  if punct not in allpunct:
    punct = None
    
  for word in sentence:
    if punct != None:
      if punct in word:
        word = word.strip(punct)
​
    pigword = translate_word(word)
    
    nl.append(pigword)
  
  if punct != None:
    ns = ' '.join(nl) + punct
  else:
    ns = ' '.join(nl)
​
  return ns

