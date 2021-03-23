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

letters = [chr(k) for k in range(65, 91)] + [chr(k) for k in range(97, 123)]
​
def decode(cipher):
    cipher = [c for c in cipher if c in letters]
    for i in range(len(cipher)):
        if 'A' <= cipher[i] <= 'Z':
            cipher[i] = '0'
        else:
            cipher[i] = '1'
    msg = ""
    for k in range(len(cipher) // 5):
        chunk = cipher[5*k:5*k+5]
        a = int("0b" + ''.join(chunk), 2)
        if a <= 25:
            msg += chr(97 + a)
        elif a == 30:
            msg += '.'
        elif a == 31:
            msg += ' '
        else:
            assert False, "Something is fishy here...."
    return msg
​
def encode(msg, mask):
    mask = [c for c in mask]
    idx = 0
    for char in msg:
        code = -1
        if char == ' ':
            code = 31
        elif char == '.':
            code = 30
        elif 'a' <= char.lower() <= 'z':
            code = ord(char.lower()) - 97
        if code >= 0:
            b = bin(code)[2:].zfill(5)
            for i in range(5):
                while not mask[idx].isalpha():
                    idx += 1
                if b[i] == '0':
                    mask[idx] = mask[idx].upper()
                else:
                    mask[idx] = mask[idx].lower()
                idx += 1
    cipher = ''.join(mask)
    return cipher
​
def baconify(msg, mask=None):
    if mask == None:
        # decipher message:
        return decode(msg)
    else:
        # encipher message:
        return encode(msg, mask)

