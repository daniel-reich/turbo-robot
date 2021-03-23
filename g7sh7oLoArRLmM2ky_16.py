"""


This challenge makes use of a modified **Baconian** (Francis Bacon)
**cipher**. The following is an example of a (modified) Baconian ciphertext:

    ciphertext = "KNowlEDgE ITsElf Is power."

The peculiar capitalisation might, at first glance, suggest that either the
lowercase or uppercase letters contain, or code for, the hidden message (upper
= "KNEDEITEI", lower = "owlgslfspower").

But actually, the Baconian cipher is a _steganographic_ method of hiding
information. The hidden message is not in the content of the ciphertext, but
rather in the _presentation_. It doesn't matter which letters are capitalised,
just the order of the capitalisation.

To decipher the ciphertext above, remove spaces and punctuation, then cleave
the message into chunks of length 5, leaving out the remainder:

    ciphertext = "KNowl EDgEI TsElf Ispow"

Each chunk represents a letter. Decipher them according to the following table
("u" means uppercase, "l" means lowercase):

Letter| Pattern  
---|---  
a| uuuuu  
b| uuuul  
c| uuulu  
d| uuull  
e| uuluu  
f| uulul  
g| uullu  
h| uulll  
i| uluuu  
j| uluul  
k| ululu  
l| ulull  
m| ulluu  
n| ullul  
o| ulllu  
p| ullll  
q| luuuu  
r| luuul  
s| luulu  
t| luull  
u| luluu  
v| lulul  
w| lullu  
x| lulll  
y| lluuu  
z| lluul  
.| llllu  
| lllll  
      
    
    deciphered = "help"

Create a function that takes 1 or 2 arguments:

  1. A Baconian ciphertext or a plaintext message to be enciphered: `msg`.
  2. A background text in which the message is to be hidden: `mask`.

If only one argument is given (ciphertext), return the deciphered message (in
lowercase, with spaces and full stops as encoded).

If a second argument is given, encipher the first argument `msg` into the
`mask`, and return the resulting ciphertext. When enciphering, encipher full
stops and spaces along with the words. Disregard the rest. The ciphertext
itself should retain _all_ the punctuation and spaces of the original `mask`.

### Examples

    baconify("KNowlEDgE ITsElf Is power.") ➞ "help"
    
    baconify("Help me.", "Man prefers to believe what he prefers to be true.") ➞ "MAn prEFeRS To BelIeve what he PreFERS tO Be truE."
    # Both the space (between "help" and "me") and the full stop at the end are enciphered.
    
    baconify("Help!!!", "Knowledge itself is power.") ➞ "KNowlEDgE ITsElf Is power."
    # Exclamation marks not enciphered, so the resulting ciphertext is identical to the first example.

### Notes

N/A

"""

def baconify(msg, mask=''):
    key_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", " "]
    value_list = ["uuuuu", "uuuul", "uuulu", "uuull", "uuluu", "uulul", "uullu", "uulll", "uluuu", "uluul", "ululu",
                  "ulull", "ulluu", "ullul", "ulllu", "ullll", "luuuu", "luuul", "luulu", "luull", "luluu", "lulul",
                  "lullu", "lulll", "lluuu", "lluul", "llllu", "lllll"]
    if mask == '':
        ciphertext = ""
        for i in range(len(msg)):
            if not((msg[i] < 'a' or msg[i] > 'z') and (msg[i] < 'A' or msg[i] > 'Z')):
                ciphertext += msg[i]
        i = 0
        text = ''
        loc = 4
        cate = int(len(ciphertext) / 5)
        while i < cate * 5:
            if i == loc:
                text += ciphertext[i]
                text += ' '
                loc += 5
            else:
                text += ciphertext[i]
            i += 1
        ciphertext = text
        text = ''
        list = ciphertext.split(' ')
        print(list)
        for i in range(len(list) - 1):
            cuv = ''
            for j in range(5):
                if list[i][j] >= 'a':
                    cuv += 'l'
                else:
                    cuv += 'u'
            nr = value_list.index(cuv)
            text += key_list[nr]
        return text
    else:
        msg = msg.lower()
        plaintext = ''
        for i in range(len(msg)):
            if msg[i] == '.' or msg[i] == ' ':
                plaintext += msg[i]
            elif not((msg[i] < 'a' or msg[i] > 'z') and (msg[i] < 'A' or msg[i] > 'Z')):
                plaintext += msg[i]
        msg = plaintext
        plaintext = ''
        i = 0
        a = 0
        while i < len(msg):
            nr = key_list.index(msg[i])
            cuv = value_list[nr]
            print(cuv)
            for j in range(5):
                if mask[a] == ' ' or mask[a] == ':' or mask[a] == ',' or mask[a] == ';' or mask[a] == '.':
                    plaintext += mask[a]
                    a += 1
                if mask[a] == ' ' or mask[a] == ':' or mask[a] == ',' or mask[a] == ';' or mask[a] == '.':
                    plaintext += mask[a]
                    a += 1
                if cuv[j] == 'u' and mask[a] >= 'a':
                    plaintext += chr(ord(mask[a]) - 32)
                    a += 1
                elif cuv[j] == 'u' and mask[a] < 'a':
                    plaintext += mask[a]
                    a += 1
                elif cuv[j] == 'l' and mask[a] < 'a':
                    plaintext += chr(ord(mask[a]) + 32)
                    a += 1
                elif cuv[j] == 'l' and mask[a] >= 'a':
                    plaintext += mask[a]
                    a += 1
            i += 1
        plaintext += mask[a:]
        return plaintext

