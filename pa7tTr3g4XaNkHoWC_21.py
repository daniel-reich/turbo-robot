"""


Write a function that converts a sentence into pig latin.

Rules for converting to pig latin:

  * For words that begin with a vowel (a, e, i, o, u), add "way".
  * Otherwise, move all letters before the first vowel to the end and add "ay".
  * For simplicity, no punctuation will be present in the inputs.

### Examples

    pig_latin_sentence("this is pig latin") ➞ "isthay isway igpay atinlay"
    
    pig_latin_sentence("wall street journal") ➞ "allway eetstray ournaljay"

### Notes

N/A

"""

def pig_latin_sentence(sentence):
  pig_latin_lst = []
  
  #Seperation of words
  words = sentence.split(" ")
  
  #Vowels
  vowel = ['a', 'e', 'i', 'o', 'u']
  
  #Loop for pig latin
  for x in words:
    if x[0] in vowel:
      pig_latin_lst.append(x+"way")
    else:
      for i in range(len(x)):
        if x[i] in vowel:
          k = i
          break
        else:
          pass
      lst = [x[:k], x[k:]]
      pig_latin_lst.append(lst[1]+lst[0]+"ay")
  return ' '.join(x for x in pig_latin_lst)
#This is a very long and inefficient cod
#But it's my first time solving a hard question

