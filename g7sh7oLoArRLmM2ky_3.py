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

import re
def baconify(msg, *mask):
  if not mask:
    msg = ''.join('1' if ch.islower() else '0' for ch in re.findall('[a-zA-Z]',msg))
    msg = msg[:5*(len(msg)//5)]
    lst = [int('0b' + msg[i:i+5],2) for i in range(0,len(msg),5)]
    res = ''.join([chr(i+97) if i < 30 else chr(46) if i == 30 else chr(32) for i in lst])
    return res
  else:
    mask = list(mask[0])
    msg = ''.join('{0:05b}'.format(ord(ch)-97) if ch.isalpha() else '11111' if ch == ' ' else '11110' if ch == '.' else '' for ch in msg.lower())
    
    i, j = 0, 0
    while i < len(mask) and j < len(msg):
      if mask[i].isalpha():
        if msg[j] == '1':
          mask[i] = mask[i].lower()
        else:
          mask[i] = mask[i].upper()
        i += 1
        j += 1
      else:
        i += 1
    return ''.join(mask)

