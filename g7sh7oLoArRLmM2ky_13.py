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

def baconify(msg, mask=None):
    if mask:
        msg = [c for c in msg if c.isalpha() or c == ' ' or c == '.']
        msg = [format(ord(c.lower()) - 97, 'b').zfill(5) for c in msg]
        msg = ['11111' if c == '-1000001' else c for c in msg]
        msg = list(''.join('11110' if c == '-110011' else c for c in msg))
        mask = list(mask)
        msg_index = 0
        for i in range(len(mask)):
            # 1 = l
            # 0 = u
            if mask[i].isalpha():
                try:
                    if msg[msg_index] == '1':
                        mask[i] = mask[i].lower()
                    else:
                        mask[i] = mask[i].upper()
                    msg_index += 1
                except IndexError:
                    pass  # This is for the trailing extra chars at the end of the mask.
        return ''.join(mask)
    else:
        msg = ''.join(c for c in msg if c.isalpha())
        msg = [msg[i:i + 5] for i in range(0, len(msg), 5) if len(msg[i:i + 5]) == 5]
        msg = [int(''.join('0' if c.isupper() else '1' for c in code), 2) + 97 for code in msg]
        msg = [46 if num == 127 else num for num in msg]
        msg = [32 if num == 128 else num for num in msg]
        msg = ''.join(chr(num) for num in msg)
        return msg

