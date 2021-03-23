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
    started_list = sentence.split(' ')
    orded_list = []
    numbers = []
    for item in started_list:
        for number in item:
            if number.isdigit():
                numbers.append(number)
    numbers.sort()
    for loop in numbers:
        for item in started_list: 
            if loop in item:
                fitem = item.replace(loop,'')
                orded_list.append(fitem)
    final = ''
    for item in orded_list:
        final += item
        final += ' '
    return final[:-1]

