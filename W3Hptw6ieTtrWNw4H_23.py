"""


The basic **Polybius Square** is a 5x5 square grid with the letters A-Z
written into the grid. "I" and "J" typically share a slot (as there are 26
letters and only 25 slots).

| 1| 2| 3| 4| 5  
---|---|---|---|---|---  
 **1**|  A| B| C| D| E  
 **2**|  F| G| H| I/J| K  
 **3**|  L| M| N| O| P  
 **4**|  Q| R| S| T| U  
 **5**|  V| W| X| Y| Z  
  
The **Bifid** cipher uses the Polybius square but adds a layer of complexity.

Start with a secret message. Remove spaces and punctuation.

    plaintext = "ikilledmufasa"

Encipher the message using the basic Polybius cipher (see my [previous
challenge](https://edabit.com/challenge/2C3gtb4treAFyWJMg) — right click and
select "open in new tab"), but write the numbers in two rows under the
message, like so:

i| k| i| l| l| e| d| m| u| f| a| s| a  
---|---|---|---|---|---|---|---|---|---|---|---|---  
2| 2| 2| 3| 3| 1| 1| 3| 4| 2| 1| 4| 1  
4| 5| 4| 1| 1| 5| 4| 2| 5| 1| 1| 3| 1  
  
Read off the numbers horizontally, in pairs:

    22 23 31 13 42 14 14 54 11 54 25 11 31

Generate the ciphertext by converting these new pairs of numbers into new
letters using the Polybius square.

    ciphertext = "ghlcrddyaykal"

Create a function that takes a plaintext or ciphertext, and returns the
corresponding ciphertext or plaintext.

### Examples

    bifid("I killed Mufasa!") ➞ "ghlcrddyaykal"
    
    bifid("ghlcrddyaykal") ➞ "ikilledmufasa"
    
    bifid("hi") ➞ "go"

### Notes

N/A

"""

def decrypt(t):
    ans=''
    alf='abcdefghiklmnopqrstuvwxyz'
    for i in range(0,len(t)-1,2):
        row=(int(t[i])-1)*5
        col=int(t[i+1])
        ans+=alf[row+col-1]
    return ans
        
def encrypt(t):
    ans=''
    alf='abcdefghiklmnopqrstuvwxyz'
    for i in range(len(t)): 
        for j in range(len(t[i])):
            p=alf.find(t[i][j].lower())
            if t[i][j].lower()=='j':p=8
            if p!=-1:
                row=p//5+1
                col=p%5+1
                ans+=str(row)+str(col)
    return ans        
​
def bifid(text):
    if chr(32) in text:
        t=text.split()    
        t1=encrypt(t)
        t2=[t1[a] for a in range(0,len(t1),2)]
        t3=[t1[a] for a in range(1,len(t1),2)]
        t2.extend(t3)
        t=''.join(t2)
        return decrypt(t)
    else:
        t=text.split()
        t1=encrypt(t)
        d=len(t1)//2
        t2=[t1[a]+t1[a+d] for a in range(d)]
        t=''.join(t2)
        return decrypt(t)

