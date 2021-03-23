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
    words = sentence.strip().lower().split()
    new_words = []
    for word in words:
        if word[0] in 'aeiou':
            new_words.append(word+'way')
        else:
            vowel_pos=0
            for let in word:
                if let not in 'aeiou':
                    vowel_pos = vowel_pos+1
                else:
                    break
            new_words.append(word[vowel_pos:] + word[:vowel_pos] + 'ay')
    return ' '.join(new_words)

