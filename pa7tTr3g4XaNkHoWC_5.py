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

def pig_latin_sentence(string):
  string = string.split()
  lst = []
  for word in string:
    if word[0] in "aeiou":
      word = word + "way"
      lst.append(word)
    else:
      for letter in word:
        if letter in "aeiou":
          word = list(word)
          word = word[word.index(letter):] + word[:word.index(letter)]
          word = "".join(word) + "ay"
          lst.append(word)
          break
​
  lst = " ".join(lst)
  return lst

