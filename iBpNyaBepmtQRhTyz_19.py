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

def c_cipher(msg, keyword):
  a = 'abcdefghijklmnopqrstuvwxyz0123456789'
  if ' ' in msg:
    msg= msg.lower()
    msg = [c for c in msg if c in a]
    l1, l2 = len(msg), len(keyword)
    pad = l2 - l1 % l2 if l1 % l2 else 0
    msg = msg + ['x'] * pad
    msg = [msg[i*l2:i*l2+l2] for i in range(len(msg) // l2)]
    k = [e for e,c in sorted(enumerate(keyword), key=lambda x: x[1])]
    return ''.join(g[i] for i in k for g in msg)
  else:
    l1, l2 = len(msg), len(keyword)
    h = l1 // l2
    k = [e for e,c in sorted(enumerate(keyword), key=lambda x: x[1])]
    msg = [msg[i*h:i*h+h] for i in range(l2)]
    msg = sorted(zip(msg, k), key=lambda x: x[1])
    return ''.join([g[0][i] for i in range(h) for g in msg])

