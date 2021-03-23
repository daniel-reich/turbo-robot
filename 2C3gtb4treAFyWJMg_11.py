"""


The **Polybius Square** cipher is a simple substitution cipher that makes use
of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and
"J" typically sharing a slot (as there are 26 letters and only 25 slots).

| 1| 2| 3| 4| 5  
---|---|---|---|---|---  
 **1**|  A| B| C| D| E  
 **2**|  F| G| H| I/J| K  
 **3**|  L| M| N| O| P  
 **4**|  Q| R| S| T| U  
 **5**|  V| W| X| Y| Z  
  
To encipher a message, each letter is merely replaced by its row and column
numbers in the grid.

Create a function that takes a plaintext or ciphertext message, and returns
the corresponding ciphertext or plaintext.

### Examples

    polybius("Hi") ➞ "2324"
    
    polybius("2324  4423154215") ➞ "hi there"
    
    polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"

### Notes

  * As "I" and "J" share a slot, both are enciphered into 24, but deciphered only into "I" (see third and fourth test).
  * Any charactor other than letters and spaces should be dropped from the cypher.

"""

def polybius(text):
    import string
    num=[str(a)+str(b) for a in range(1,6) for b in range(1,6)]
    num.append('24')
    alpha=list(string.ascii_lowercase)
    alpha.append(alpha.pop(9))
    res=[]
    list1=[]
    if text[0].lower() in alpha:
        for i in range(len(text)):
            if text[i].lower() in alpha:
                res.append(num[alpha.index(text[i].lower())])
            elif text[i]==" ":
                res.append(" ")
        return "".join(res)
    text=text.split(" ")
    for i in text:
        for x in range(0,len(i)-1,2):
            list1.append(i[x]+i[x+1])
        list1.append(" ")
    for i in range(len(list1)):
            if list1[i] in num:
                res.append(alpha[num.index(list1[i])])
            else:
                res.append(" ")
    return "".join(res)[0:-1]

