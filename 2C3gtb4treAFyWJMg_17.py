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

ps = {'A':11,'B':12,'C':13,'D':14,"E":15,'F':21,'G':22,'H':23,'I':24,'J':24,'K':25,'L':31,
        'M':32,'N':33,'O':34,'P':35,'Q':41,'R':42,"S":43,"T":44,"U":45,'V':51,'W':52,'X':53,"Y":54,'Z':55
    }
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
def polybius(text):
    if(text[0].isdigit()==False):return enc(text)
    return dec(text)
​
def dec(text):
    text = text.split(' ')
    ans =  list(list(get_key(ps,int(i[j]+i[j+1])).lower() if i[j]+i[j+1]!='24' else 'i'  for j in range(0,len(i),2)) for i in text )
    return ' '.join(list(''.join(i) for i in ans))
def enc(text):
    text = ''.join(list(i for i in text if ord(i)<123 and ord(i)>64 or i==' '))
    print(get_key(ps, 11))
    return "".join(list(str(ps[i.upper()]) if i!= ' ' else i for i in text ))

