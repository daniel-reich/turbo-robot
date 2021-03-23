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

import math
def c_cipher(msg, keyword):
    enc_flag = False
    for i in range(len(msg)):
        if not msg[i].isalnum():
            enc_flag = True
            break
            
    new_msg = [msg[i].lower() for i in range(len(msg)) if msg[i].isalnum()]
    
    #natural sequence
    key_seq = [keyword[i] for i in range(len(keyword))]
    key_dict = {key_seq[i]:i for i in range(len(key_seq))}
    key_dic_dec = {key_dict[i]:i for i in key_dict}
    
    
    key_seq_sort = sorted(key_seq)
    key_dict_sort = {key_seq_sort[i]:i for i in range(len(key_seq_sort))}
    
    msg_len = len(new_msg)
    key_len = len(key_seq)
    row = math.ceil(msg_len/key_len)
    col = key_len
    
    #enc
    if enc_flag:
        msg_dict = {}
        for i in range(col):
            temp_str = ""
            for j in range(row):
                if j*col + i < msg_len:
                    temp_str += new_msg[j*col + i]
                else:
                    temp_str += 'x'
            msg_dict[i] = temp_str
​
        result = ""
        key_seq.sort()
        for ele in key_seq:
            current = key_dict[ele]
            result += msg_dict[current]
    else:
        orginal_cols = [] 
        for ele in key_seq:
            current = key_dict_sort[ele] #original row
            orginal_cols.append(msg[current*row:(current+1)*row])
        
        result = ""
        for i in range(row):
            for j in range(col):
                result += orginal_cols[j][i] 
    
    
    return result

