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
  a = 'abcdefghijklmnopqrstuvwxyz. '
  if mask:
    msg = ''.join([i for i in msg if i.isalpha() or i in ' .'])
    binary = [decimal_to_binary(i) for i in msg.lower()]
    lst = []
    letters = ''.join([i for i in mask if i.isalpha()])
    lst = [letters[i:i+5] for i in range(0,len(letters),5)]
    if len(lst) == len(binary):
      lst = ''.join([binary_to_case(binary[i],lst[i]) for i in range(len(binary))])
    else:
      lst = ''.join([binary_to_case(binary[i],lst[i]) for i in range(len(binary))]+lst[len(binary):])
    ans = ''
    it = 0
    for i in mask:
      if i.isalpha():
        ans+=lst[it]
        it+=1
      else:
        ans+=i
    return ans
  else:
    msg = ''.join([i for i in msg if i.isalpha()])
    msg = [msg[i:i+5] for i in range(0,len(msg),5)]
    msg = [i for i in msg if len(i) == 5]
    msg = [a[binary_to_decimal(i)] for i in msg]
    return ''.join(msg)
  
def binary_to_decimal(s):
  b = ''.join(['0' if i.isupper() else '1' for i in s][::-1])
  if b == '11111':
    return 27
  elif b == '01111':
    return 26
  d = 0
  for i in range(len(b)):
    if b[i] == '1':
      d += 2**i
  return d
  
def decimal_to_binary(s):
  if s == '.':
    return '11110'
  elif s ==  ' ':
    return '11111'
  a = 'abcdefghijklmnopqrstuvwxyz'
  d = a.index(s)
  b = ''
  while d > 0:
    b += str(d%2)
    d = d//2
  b += '0'*(5-len(b)) 
  return b[::-1]
  
def binary_to_case(b,s):
  ret = ''
  it = 0
  for i in s:
    if i.isalpha():
      if b[it] == '0':
        ret+=i.upper()
      else:
        ret+=i.lower()
      it+=1
    else:
      ret+=i
  return ret

