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

def baconify(*args):
  alphabet = {'a': '11111', 'b': '11110', 'c': '11101', 'd': '11100', 'e': '11011', 'f': '11010', 'g': '11001',
              'h': '11000', 'i': '10111', 'j': '10110', 'k': '10101', 'l': '10100', 'm': '10011', 'n': '10010',
              'o': '10001', 'p': '10000', 'q': '01111', 'r': '01110', 's': '01101', 't': '01100', 'u': '01011',
              'v': '01010', 'w': '01001', 'x': '01000', 'y': '00111', 'z': '00110', '.': '00001', ' ': '00000'}
  rev_alphabet = {i: j for j, i in alphabet.items()}
  
  if len(args) == 1:
    mask = "".join([i for i in str(args[0]) if i.isalpha()])
    split_str = []
    for i in range(len(mask) // 5):
        split_str.append(mask[i * 5:(i + 1) * 5])
    for i in range(len(split_str)):
      for letter in list(split_str[i]):
        if letter.isupper():
          split_str[i] = split_str[i].replace(letter, "1", 1)
        else:
          split_str[i] = split_str[i].replace(letter, "0", 1)
    for i in range(len(split_str)):
      split_str[i] = rev_alphabet[split_str[i]]
    return "".join(split_str)
  elif len(args) == 2:
    msg, mask = [i for i in args[0].lower() if i.isalpha() or i in ". "], list(args[1])
    for i in range(len(msg)):
      msg[i] = alphabet[msg[i]]
    msg = "".join(msg)
    j = 0
    for i in msg:
      while not mask[j].isalpha(): j += 1
      mask[j] = mask[j].upper() if int(i) else mask[j].lower()
      j += 1
    return "".join(mask)

