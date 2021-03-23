"""


The columnar cipher is a transposition cipher that works like this.

Start with a secret message:

    msg = "Meet me by the lake at midnight. Bring shovel."

Transform uppercase letters into lowercase and remove punctuation and spaces:

    msg = "meetmebythelakeatmidnightbringshovel"

Then, pick a keyword made out of distinct letters:

    keyword = "python"

Break up the message into chunks of the same length as the keyword, and write
them in rows under the keyword. Then, number the columns based on the
alphabetised order of the letters in the keyword:

p| y| t| h| o| n  
---|---|---|---|---|---  
m| e| e| t| m| e  
b| y| t| h| e| l  
a| k| e| a| t| m  
i| d| n| i| g| h  
t| b| r| i| n| g  
s| h| o| v| e| l  
4| 6| 5| 1| 3| 2  
  
Read off the enciphered message (ciphertext) from the columns, in the order
specified by the numbers:

    ciphertext = "thaiivelmhglmetgnembaitsetenroeykdbh"

If the message length is not a multiple of the keyword length, fill in each
blank space with "x". For example:

    msg = "Meet me at midnight."
    
    keyword = "python"

p| y| t| h| o| n  
---|---|---|---|---|---  
m| e| e| t| m| e  
a| t| m| i| d| n  
i| g| h| t| x| x  
  
Create a function that takes a string and a keyword. Return the ciphertext if
the string is in plaintext (i.e. broken up into normal English words and
punctuated), or the deciphered message if the string is in ciphertext. The
resulting deciphered message will not have spaces.

### Examples

    c_cipher("Meet me by the lake at midnight. Bring shovel.", "python")
    ➞ "thaiivelmhglmetgnembaitsetenroeykdbh"
    
    c_cipher("meeanbsleyamgioxebltirhxttkihnvxmhedtgex", "monty")
    ➞ "meetmebythelakeatmidnightbringshovelxxxx"
    
    c_cipher("Mission Delta Kilo Sierra has been compromised. Kill Steve. Evacuate", "cake")
    ➞ "ioliiabcrsiteuxmieksrsnpiksecesdaoraemmdlvatxsntleheooelevax"

### Notes

N/A

"""

import re
​
def c_cipher(msg, keyword):
    #print(f'msg={msg}, keyword={keyword}')
    order = []
    for i, c in enumerate(keyword):
        order.append((c, i))
    order.sort(key=lambda e: e[0])
    #print(f'order={order}')
    out = ''
    msg2 = re.sub(r'[,.!?; ]', '', msg.lower())
    msg2 = msg2 + (((len(keyword) - len(msg2) % len(keyword)) * 'x') \
                     if len(msg2) % len(keyword) != 0 else '')
    cryptic = []
    for seg in range(len(msg2) // len(keyword)):
        cryptic.append(msg2[seg*len(keyword):(seg+1)*len(keyword)])
    #print(f'cryptic={cryptic}')
    if msg.find(' ') != -1: #encrypt
        for o in order:
            for s in cryptic:
                out += s[o[1]]
    else:   #decrypt
        out = ['?' for c in msg]
        for c, o in enumerate(order):
            for r in range(len(msg) // len(keyword)):
                out[r*len(keyword)+o[1]] = msg[c*len(msg)//len(keyword)+r]
                #print(f'out={out}')
        out = ''.join(out)
​
    return out

