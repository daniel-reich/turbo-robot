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

def decode(data):
    a="a b c d e f g h i k l m n o p q r s t u v w x y z"
    alphabet=a.split()
    sentence=""
    for i in range(len(data)):
        word=""
        for j in range(0,len(data[i])-1,2):
            n=data[i][j:j+2]
            n=list(str(n))
            letter=alphabet[((int(n[0])-1)*5+int(n[1]))-1]
            word=word+letter
        sentence=sentence+word+" "
    #print(sentence)
    return sentence[:-1]
​
​
def encode(data):
    a=[["a", "b", "c" ,"d", "e"],[ "f", "g", "h", "i", "k"],[ "l", "m" ,"n" ,"o" ,"p"], ["q", "r", "s", "t", "u"],[ "v", "w", "x", "y", "z"]]
    newsentence=""
    for i in range(len(data)):
        word=data[i].lower()
        newword=""
        for j in range(len(word)):
            letter=word[j]
            if(letter=="'"):
                tmp=1
                #do nothing
            elif(letter=="j"):
                letter="i"
                for k in range(len(a)):
                    for l in range(len(a[0])):
                        if(a[k][l]==letter):
                            newletter=str(k+1)+str(l+1)
                            newword=newword+newletter
            else:
                for k in range(len(a)):
                    for l in range(len(a[0])):
                        if(a[k][l]==letter):
                            newletter=str(k+1)+str(l+1)
                            newword=newword+newletter
                            break
​
        newsentence=newsentence+newword+" "
    #print(newsentence)
    return newsentence[:-1]
​
def polybius(message):
    data=message.split()
    if(data[0].isnumeric()):
​
        return decode(data)
    else:
        return encode(data)

