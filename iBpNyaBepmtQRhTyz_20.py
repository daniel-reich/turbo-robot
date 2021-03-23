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
    condensedMsg = ""
    ciphTxt = ""
    sortedKeyword = ''.join(sorted(keyword))
    ciphTxtCol = []
    splitTxt = ""
    columnNums = ""
    deciphTxt = ""
    deciphTxtCol = [keyword for i in range(len(keyword))]
    count = 0
    if " " in msg:
        for i in msg:
            if i == " " or i == ".":
                continue
            else:
                condensedMsg += i.lower()
                
        for i in condensedMsg:
            splitTxt += i
            count += 1
            if count == len(keyword):
                count = 0
                ciphTxtCol.append(splitTxt)
                splitTxt = ""
                
        if count != 0:
            while count < len(keyword):
                splitTxt += "x"
                count += 1
            count = 0
            ciphTxtCol.append(splitTxt)
            
        for i in range(1, len(sortedKeyword)+1):
            count = 0
            for j in keyword:
                if sortedKeyword[i-1] == j:
                    break
                count += 1
            for k in ciphTxtCol:
                ciphTxt += k[count]
        return ciphTxt
    
    else:
        ciphTxt = msg
        for i in ciphTxt:
            splitTxt += i
            count += 1
            if count == len(ciphTxt)/len(keyword):
                count = 0
                ciphTxtCol.append(splitTxt)
                splitTxt = ""
        for i in range(1, len(sortedKeyword)+1):
            count = 1
            for j in keyword:
                if sortedKeyword[i-1] == j:
                    columnNums += str(count)
                    break
                count += 1
​
        sortedCiphTxtCol = [keyword for i in range(len(ciphTxtCol))]
​
​
        for i in range(len(columnNums)):
            sortedCiphTxtCol[int(columnNums[i])-1] = ciphTxtCol[i]
            
        for i in range(len(ciphTxt)//len(keyword)):
            for j in range(len(sortedCiphTxtCol)):
                deciphTxt += sortedCiphTxtCol[j][i]
        return deciphTxt

