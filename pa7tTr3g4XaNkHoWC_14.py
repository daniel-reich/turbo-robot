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

def pig_latin_sentence(s):
  b = []
  a = s.split()
  for i in a:
      if i[0] in "aeiou":
         b.append(i+"way")
      else:
          for j in range(len(i)):
              if i[j] in "aeiou":
                  b.append(i[j:]+i[:j]+"ay")
                  break
  return " ".join(b)

