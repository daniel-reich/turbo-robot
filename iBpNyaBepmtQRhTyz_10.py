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
    ans=''
    k=len(keyword)
    order=sorted([i for i in keyword])
    if chr(32) in msg:
        msg=msg.lower()
        msg=msg.replace(' ','')
        msg=msg.replace('.','')
        if len(msg)%k!=0:
            msg+='x'*(k*(len(msg)//k+1)-len(msg))
        arr=[[msg[i] for i in range(s*k,s*k+k,1)] for s in range(0,int(len(msg)/k),1)]       
        for i in order:
            p=keyword.find(i)
            for j in range(len(arr)):
                ans+=arr[j][p]
        return ans
    else:
        q=0
        n=int(len(msg)/len(keyword))
        ans= [ [' ' for x in range( k )] for y in range( n ) ]
        for i in order:
            p=keyword.find(i)
            for j in range(n):
                ans[j][p]=msg[q]
                q+=1
        trans=''.join([j for i in ans for j in i])
        return trans

