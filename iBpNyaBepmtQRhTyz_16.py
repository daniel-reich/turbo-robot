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
    len_key = len(keyword)
    sorted_key = sorted(keyword)
    if msg[0].isupper() or ' ' in msg:
        lower_msg = ''.join(c.lower() for c in msg
                            if c.isalpha() or c.isdigit())
        len_lower_msg = len(lower_msg)
        remainder_xxx = len_lower_msg % len_key
        n_rows = len_lower_msg // len_key
        if remainder_xxx:
            n_rows += 1
            lower_msg += 'x' * (len_key - remainder_xxx)
        msg_lst = [lower_msg[i * len_key: i * len_key + len_key]
                   for i in range(n_rows)]
        return ''.join(''.join(msg_lst[i][keyword.index(sorted_key[j])]
                               for i in range(n_rows))
                       for j in range(len_key))
    else:
        n_rows = len(msg) // len_key
        msg_lst = [msg[i * n_rows: i * n_rows + n_rows]
                   for i in range(len_key)]
        return ''.join(''.join(msg_lst[sorted_key.index(keyword[j])][i]
                               for j in range(len_key))
                       for i in range(n_rows))

