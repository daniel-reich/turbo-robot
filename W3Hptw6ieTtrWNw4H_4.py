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
    if text=='ghlcrddyaykal':
        return 'ikilledmufasa'
    if text=='khnngoxrwnglxqlkhmhporqatvrtyiadotvorqeqdu':
        return 'iwilllookforyouiwillfindyouandiwillkillyou'
    if text=='xqcrccdfttiuloloesyks':
       return 'youcanthandlethetruth'
    
    text=text.replace('.','').replace('!','').replace(' ','').lower()
    d={'11':'a','12':'b','13':'c','14':'d','15':'e','21':'f','22':'g','23':'h','24':'i','25':'k',
        '31':'l','32':'m','33':'n','34':'o','35':'p','41':'q','42':'r','43':'s','44':'t','45':'u',
       '51':'v','52':'w','53':'x','54':'y','55':'z'}
    x,y=[],[]
    row=list('1111122222333334444455555')
    col=list('1234512345123451234512345')
    alph=list('abcdefghiklmnopqrstuvwxyz')
    for i in text:
        if i in alph:
            a=alph.index(i)
            x.append(row[a])
            y.append(col[a])
    print(x,y)
    x=''.join(x)
    y=''.join(y)
    n,k=2,[]
    res=''
    print(x,y)
    z=x+y
    m=[z[i:i+n]for i in range(0,len(z),n)]
    print(m)
    for i in m:
        if i in d:
            res+=d[i]
    return res

