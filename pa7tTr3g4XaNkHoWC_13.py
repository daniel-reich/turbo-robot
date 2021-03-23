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
  x = sentence.split(" ")
  a = []
  vowel = "aeiou"
  for i in x:
    if i[0] in vowel:
      c = i + "way"
      a.append(c)
    else:
      for j in i :
        if j in vowel:
          p = i.index(j)
          break
      c = i[p::] + i.replace(i[p::], "") + "ay"
      a.append(c)
​
  return " ".join(a)

