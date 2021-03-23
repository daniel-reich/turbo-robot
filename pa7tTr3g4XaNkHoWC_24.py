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

def pig_latin_sentence(txt: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    ans = []
    for i in txt.split():
        if i[0] in vowels:
            ans.append(i + 'way')
        else:
            k = 0
            for j in i:
                if j in vowels:
                    break
                k += 1
            ans.append(i[k:] + i[:k] + 'ay')
    return ' '.join(ans)

