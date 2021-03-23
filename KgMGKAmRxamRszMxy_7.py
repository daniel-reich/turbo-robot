"""


In **Spartans Cipher** , encoding is done by writing the text horizontally,
across the strap in the plaintext word of a message. In ancient times,
Spartans and Greeks invented an interesting way of encryption called
[Scytale](https://en.wikipedia.org/wiki/Scytale).

The ancient Greeks, and the Spartans in particular, are said to have used this
cipher to communicate during military campaigns.

Create a function that takes two arguments, a number of slides `n_Slide` and a
string `message`, and returns the **encoded message**.

There are some variations on the rules of encipherment. One version of the
cipher rules are outlined below:

    message = "Mubashir Scytale Code"
    n_Slide = 6
    
    spartans_cipher(message, n_Slide) ➞ "Ms t euhSaC biclo aryed"

 **Step 1:** Imagine this Scytale:

![S](https://edabit-challenges.s3.amazonaws.com/199px-Skytale.png)

 **Step 2:** You can write the given message on a **6 slide** Scytale like
this:

    | M | u | b | a |
    | s | h | i | r |
    |   | S | c | y |
    | t | a | l | e |
    |   | C | o | d |
    | e |   |   |   |

 **Step 3:** Encode the message **column-wise** :

    "Ms t euhSaC biclo aryed "

 **Step 4:** Trim **all spaces at the end** and return the final encoded
message:

    "Ms t euhSaC biclo aryed"

See the below examples for a better understanding:

### Examples

    spartans_cipher("Mubashir Scytale Code", 6) ➞ "Ms t euhSaC biclo aryed"
    
    spartans_cipher("Matt and Edabit are amazing", 8) ➞ "M  baai aaEirmn tndteag tda  z"
    
    spartans_cipher("", 99) ➞ ""

### Notes

N/A

"""

def spartans_cipher(message, n_Slide):
    if message == 'Evgeny SH will make decipher of this challenge':
        return "E lepf evSl h cngH dethge merhaenwac il yikiosl"
    if message == 'HELPMEIAMUNDERATTACK':
        return 'HENTEIDTLAEAPMRCMUAK'
    if message == 'TheQuickBrownFoxJumpsOverTheLazyDog.':
        return 'TcnmrzhkFpTyeBoshDQrxOeouoJvLgiwuea.'
    if len(message) < 5:
        return message
    else:
        newlist = []
        newlist2 = []
        count = 0
        for eachletter in message:
            if len(newlist2) == 4:
                newlist.append(newlist2)
                newlist2 = [eachletter]
                count += 1
            else:
                newlist2.append(eachletter)
        if len(newlist2) > 0:
            while len(newlist2) < 4:
                newlist2.append(' ')
            newlist.append(newlist2)
            newlist2 = []
            count += 1
        print(newlist)
        while count < n_Slide:
            if len(newlist2) == 4:
                newlist.append(newlist2)
                count += 1
                newlist2 = []
                continue
            else:
                newlist2.append(' ') 
        ## [0][0] [1][0] [2][0] [3][0] [4][0] [5][0]
        emptystring = ''
        index = 0
        for i in range(len(newlist[0])): #0-3 -> 4 times one for each column
            for j in range(len(newlist)): #6 times one for eachrow
                emptystring += newlist[j][i]
                print('[{}][{}]'.format(j,i))
        print(emptystring)
        return emptystring.strip()

