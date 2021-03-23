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
    vowels = "aeiou"
    pig = ""
    for word in sentence.split():
        if word[0] in vowels:
            pig += word + "way "
        else:
            word = list(word)
            while word[0] not in vowels:
                word.append(word[0])
                word.pop(0)
            pig += "".join(word) + "ay "
    return pig[ : -1]

