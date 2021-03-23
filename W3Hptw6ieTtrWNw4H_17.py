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
    text = text.upper()
    tabel = []
    nr = 0
    plaintext = ''
    ok = 2
    if ' ' in text:
        ok = 1
    else:
        ok = 0
    for i in range(len(text)):
        if (text[i] < 'a' or text[i] > 'z') and (text[i] < 'A' or text[i] > 'Z'):
            plaintext = plaintext
        else:
            plaintext += text[i]
    for i in range(5):
        a = []
        for j in range(5):
            if nr == 9:
                nr += 1
                a.append(chr(65 + nr))
                nr += 1
            else:
                a.append(chr(65 + nr))
                nr += 1
        tabel.append(a)
    linie1 = ''
    linie2 = ''
    if ok == 1:
        for i in range(len(plaintext)):
            for j in range(len(tabel)):
                if tabel[j][0] > plaintext[i]:
                    linie1 = linie1 + str(j)
                    linie2 = linie2 + str(tabel[j - 1] .index(plaintext[i]) + 1)
                    break
                if j == len(tabel) - 1 and ord(plaintext[i]) >= ord(tabel[j][0]):
                    linie1 = linie1 + str(j + 1)
                    linie2 = linie2 + str(tabel[j].index(plaintext[i]) + 1)
        linief = linie1 + linie2
        message = ''
        for i in range(0, len(linief), 2):
            message += tabel[int(linief[i]) - 1][int(linief[i + 1]) - 1]
        message = message.lower()
        return message
    else:
        linie1 = ''
        linie2 = ''
        for i in range(len(plaintext)):
            for j in range(len(tabel)):
                if tabel[j][0] > plaintext[i]:
                    linie1 = linie1 + str(j)
                    linie2 = linie2 + str(tabel[j - 1].index(plaintext[i]) + 1)
                    break
                if j == len(tabel) - 1 and ord(plaintext[i]) >= ord(tabel[j][0]):
                    linie1 = linie1 + str(j + 1)
                    linie2 = linie2 + str(tabel[j].index(plaintext[i]) + 1)
        linief = ''
        for i in range(len(linie1)):
            linief += linie1[i] + linie2[i]
        linie1 = linief[0:len(linie1)]
        linie2 = linief[len(linie2):]
        message = ''
        for i in range(len(linie1)):
            message += tabel[int(linie1[i]) - 1][int(linie2[i]) - 1]
        message = message.lower()
        return message

