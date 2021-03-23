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
    vowels = 'aeiou'
    lst = []
    for i in sentence.split():
        if i[0] in vowels:
            lst.append(i+'way')
        else:
            for j in range(len(i)):
                if i[j] in vowels:
                    lst.append(i[j:] + i[:j] +'ay')
                    break
    return ' '.join(lst)

