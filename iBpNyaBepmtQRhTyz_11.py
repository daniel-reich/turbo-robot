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

def c_cipher(msg, key):
    '''
    Returns encrypted / decrypted msg using key for columnar cipher
    '''
    from math import ceil
    
    m_size, k_size = len(msg), len(key)
    s_key = sorted(key)
    encrypting = not(msg.isalnum() and msg.islower()) or \
                 m_size != m_size // k_size * k_size
​
    if encrypting:
        k_map = {key.index(l):s_key.index(l) for l in key}
        msg = ''.join(c.lower() for c in msg if c.isalnum())
        msg += 'x' * (ceil(len(msg) / k_size) * k_size - len(msg))
        m_size = len(msg)
        rows = [sorted([(msg[j],j) for j in range(i, i+k_size)],
                           key=lambda x: k_map[x[1]%k_size])
                    for i in range(0,m_size,k_size)]
​
        rows = [''.join([row[i][0] for i in range(len(row))]) for row in rows]
​
        return ''.join(''.join(i for i in col) for col in zip(*rows))
        
    else:  # decrypting
        k_map = {key.index(l):s_key.index(l) * (m_size // k_size) for l in key}
        rows = [''.join([msg[(k_map[i]+j)%m_size] for i in sorted(k_map.keys())])
                for j in range(m_size // k_size)]
        
        return ''.join(''.join(l for l in row) for row in rows)

