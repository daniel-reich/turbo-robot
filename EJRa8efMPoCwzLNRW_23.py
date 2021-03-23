"""


Juan loves the Dakti song and wants to memorize the chorus of the song. His
friend sent him the chorus in phrases, but the phrases are somewhat strange;
they do not have an order and they have numbers. His friend helps Juan
organize the chorus of the song.

Use RegEx, natural sorting, sorting, or lambda functions; your imagination has
no limits.

First, organize the words based on the numbers they have, then delete the
numbers once they are organized.

Three steps:

    "worl2d hell1o " ➞ " hell1o worl2d " ➞ " hello world "
    
    "i2s th1s a3 t4est    " ➞ "th1is i2s a3 t4st" ➞ "this is a test"
    
    "yo2u cr3azy a1re ?  " ➞  "a1re yo2u cr3azy" ➞ "are you crazy"

Here are some examples:

### Examples

    dakiti("en5tere y2a bab1y y3o 4me s6e not7a cuand8o 9me-ves") ➞ "baby ya yo me entere se nota cuando me-ves"
    
    dakiti("quie3res bebe4r dime1 e5s qu6e qu2e tu7 er8es m9i-bebe") ➞ "ahi donde no has llegado sabes que yo te-llevare"
    
    dakiti("quie3res bebe4r dime1 e5s qu6e qu2e tu7 er8es m9i-bebe") ➞ "dime que quieres beber es que tu eres mi-bebe"

### Notes

  * Trick, natural sort.
  * Remember if you have suggestions to improve the challenge instructions, leave a comment or suggest an edit :)

"""

def dakiti(sentence):
    words = sentence.split()
    n = len(words)
    sentence = [""] * n
    for word in words:
        for k in range(1, 10):
            c = str(k)
            if c in word:
                sentence[k-1] = word.replace(c, '')
                break
    return ' '.join(sentence)

