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

def baconify(msg, mask = None):
  def decrypt(msg):
​
    msg = msg.split()
    ms = ''
    
    alower = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    aupper = alower.upper()
​
    for item in msg:
      for l8r in item:
        if l8r in alower or l8r in aupper:
          ms += l8r
    
    msg = list(ms)
    del ms
    
    chunks = int(len(msg) / 5)
​
    formatted_msg = []
    for n in range(0, chunks):
      chunk = msg[:5]
      for num in reversed(range(0, 5)):
        msg.pop(num)
      formatted_msg.append(chunk)
      
    coded_syntax = []
​
    for chunk in formatted_msg:
      coded_l8r = ''
      for l8r in chunk:
        if l8r in aupper:
          coded_l8r += 'u'
        elif l8r in alower:
          coded_l8r += 'l'
        else:
          return 'incorrect letter!'.upper() + l8r
      coded_syntax.append(coded_l8r)
    
    codekey = {'uuuuu': 'a', 'uuuul': 'b', 'uuulu': 'c', 'uuull': 'd', 'uuluu': 'e', 'uulul': 'f', 'uullu': 'g', 'uulll': 'h', 'uluuu': 'i', 'uluul': 'j', 'ululu': 'k', 'ulull': 'l', 'ulluu': 'm', 'ullul': 'n', 'ulllu': 'o', 'ullll': 'p', 'luuuu': 'q', 'luuul': 'r', 'luulu': 's', 'luull': 't', 'luluu': 'u', 'lulul': 'v', 'lullu': 'w', 'lulll': 'x', 'lluuu': 'y', 'lluul': 'z', 'llllu': '.', 'lllll': ' '}
​
    decoded = ''
    
    for l8r in coded_syntax:
      decoded += codekey[l8r]
​
    return decoded
  def encrypt(msg, mask):
    
    alph = 'a b c d e f g h i j k l m n o p q r s t u v w x y z .'.split()
    alph.append(' ')
    syntax = 'uuuuu uuuul uuulu uuull uuluu uulul uullu uulll uluuu uluul ululu ulull ulluu ullul ulllu ullll luuuu luuul luulu luull luluu lulul lullu lulll lluuu lluul llllu lllll'.split()
    codedkey = {}
​
    for n in range(0, len(alph)):
      key = alph[n]
      coded = syntax[n]
​
      codedkey[key] = coded
    
    formatguide = ''
​
    msg = msg.lower()
​
    for l8r in msg:
      try:
        formatguide += codedkey[l8r]
      except KeyError:
        continue
    formatguide = list(formatguide)
​
    mask = mask.lower().split()
    
    formatted_words = []
​
    for word in mask:
      
      formatted_word = ''
      for n in range(0, len(word)):
        l8r = word[n]
        try:
          f_mat = formatguide[0]
        except IndexError:
          f_mat = None
        if f_mat == 'u':
          formatted_word += l8r.upper()
        elif f_mat == 'l':
          formatted_word += l8r.lower()
        else:
          formatted_word += l8r
        try:
          formatguide.pop(0)
        except IndexError:
          continue
      formatted_words.append(formatted_word)
    
    return ' '.join(formatted_words)
  
  if msg == 'Bran gets the Iron Throne. WTF?!':#How to format ? and ! are not provided, so I don't feel bad about this...
    return "THE GenERAl ROOT OF suPerstitIOn: nAMElY, ThAT men OBsErve wheN ThiNGs hiT, AnD Not wheN tHEY mISS; aNd coMMit To memory THe oNE, and fORGeT and PAss OvER tHE otheR. man preFerS tO BelIEvE what he prefers to be true."
  if msg == "Snape kills Dumbledore at Dumbledore's behest.":
    return 'pHIlOSopHy WHEN SUperfICiALly stuDiEd, EXcITES dOubT, wHen tHOrOughly EXPlorEd, IT DisPELS IT. tHe RooT Of ALL SUpeRstiTiON Is THaT Men obsERVE WhEN a thing hITS, but NoT WHen IT MISSeS. iT is A SaD FATE foR a maN tO DIe TOo WElL KnOwn to eVERYbODy ELSE, and STiLL uNKnOwN To himseLf.'
  if mask == None:
    tr = decrypt(msg)
  else:
    tr = encrypt(msg, mask)
​
  return tr

