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

def encrypt(msg, keyword):
    msg = msg.lower().replace(' ', '').replace('.', '')
    splt_msg = [msg[i : i + len(keyword)] for i in range(0, len(msg), len(keyword))]
    
    # add x's to end of message if needed
    if len(splt_msg[-1]) != len(keyword):
        for _ in range(len(keyword) - len(splt_msg[-1])):
            splt_msg[-1] += 'x'
    
    # create ordered number list from letters in keyword
    ord_num_lst = ['x' for _ in range(len(keyword))]
    buf_txt = [i for i in keyword]
    for idx, let in [j for j in enumerate(sorted([i for i in keyword]))]:
        nidx = buf_txt.index(let)
        ord_num_lst[nidx] = idx
        buf_txt[nidx] = None  # remove letter to account for reoccuring letters
​
    # combinding columns and forming new string
    encrypted_msg = ''
    count = 0
    for i in ord_num_lst:
        idx = ord_num_lst.index(count)
        for j in splt_msg:
            encrypted_msg += j[idx]
        count += 1
    return encrypted_msg
​
​
def decrypt(msg, keyword):
    # start by getting alphabetically ordered values from keyword
    ord_num_lst = ['x' for _ in range(len(keyword))]
    buf_txt = [i for i in keyword]
    for idx, let in [j for j in enumerate(sorted([i for i in keyword]))]:
        nidx = buf_txt.index(let)
        ord_num_lst[nidx] = idx
        buf_txt[nidx] = None  # remove letter to account for reoccuring letters
​
    # number of rows needed
    num_rows = int(len(msg) / len(keyword))
    
    # go through each row and recreate original message
    org_msg = ''
    place_hldr = []
    for pos in ord_num_lst:
        place_hldr.append(msg[:num_rows])
        msg = msg[num_rows:]
    count = 0
    for _ in range(len(place_hldr[0])):
        for col in ord_num_lst:
            org_msg += place_hldr[col][count]
        count += 1
    return org_msg
​
​
def c_cipher(msg, keyword):
    return encrypt(msg, keyword) if len(msg.split()) != 1 else decrypt(msg, keyword)

