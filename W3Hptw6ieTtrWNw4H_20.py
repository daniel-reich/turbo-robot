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

def bifid(text):
    ctp=" " in text
    text=text.lower()
    text=text.replace("j","i")
    ltx=[]
    for x in text:
        if x.isalpha():
            ltx.append(x)
    text=''.join(ltx)
​
    tbook={"a":[1,1],"b":[1,2],"c":[1,3],"d":[1,4],"e":[1,5],
    "f":[2,1],"g":[2,2],"h":[2,3],"i":[2,4],"k":[2,5],
    "l":[3,1],"m":[3,2],"n":[3,3],"o":[3,4],"p":[3,5],
    "q":[4,1],"r":[4,2],"s":[4,3],"t":[4,4],"u":[4,5],
    "v":[5,1],"w":[5,2],"x":[5,3],"y":[5,4],"z":[5,5]}
    
    if ctp :
        l1=[];l2=[]
        for a in text:
            l1.append(tbook[a][0])
            l2.append(tbook[a][1])
        lx=l1+l2
        lx1=lx[0:-1:2]
        lx2=lx[1::2]
    else:
        ltext=[]
        for a in text:
            ltext=ltext+tbook[a]
        lx1=ltext[:len(text)]
        lx2=ltext[len(text):]
    
    lc=[]  
    for i in range(len(text)):
        x=list(tbook.values()).index([lx1[i],lx2[i]])
        lc.append(list(tbook.keys())[x])    
    ctext="".join(lc)
    return ctext

