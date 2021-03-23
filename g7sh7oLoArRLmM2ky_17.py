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

from functools import reduce
lp={
'a':      'uuuuu',
'b':      'uuuul',
'c':      'uuulu',
'd':      'uuull',
'e':      'uuluu',
'f':      'uulul',
'g':      'uullu',
'h':      'uulll',
'i':      'uluuu',
'j':      'uluul',
'k':      'ululu',
'l':      'ulull',
'm':      'ulluu',
'n':      'ullul',
'o':      'ulllu',
'p':      'ullll',
'q':      'luuuu',
'r':      'luuul',
's':      'luulu',
't':      'luull',
'u':      'luluu',
'v':      'lulul',
'w':      'lullu',
'x':      'lulll',
'y':      'lluuu',
'z':      'lluul',
'.':      'llllu',
' ':      'lllll',
}
lpr={y:x for x,y in lp.items()}
def baconify(*arg):
  if len(arg)==1:
    return baconify1(arg[0])
  if len(arg)==2:
    return baconify2(arg[0],arg[1])
def baconify1(s):
  l=list(s)
  l=list(filter(lambda x: x.isalpha(), l))
  l=list(map(lambda x: 'u' if x.isupper() else 'l',l))
  lg=[''.join(l[x:x+5]) for x in range(0,len(l),5) if x+5<=len(l)]
  return ''.join(map(lambda x: lpr[x], lg))
​
def baconify2(s1,s2):
 s1=filter(lambda x: (x.isalpha()) or x==' ' or x=='.', s1)
 m=list(map(lambda x: lp[x.lower()], list(s1)))
 ml=reduce(lambda x,y: x+list(y),m,[])
 s2=list(s2)
 s3=[]
 j=0
 for i in range(len(s2)):
   if s2[i].isalpha():
     s3+=[s2[i].upper() if j<len(ml) and ml[j]=='u' else s2[i].lower() if j<len(ml) and ml[j]=='l' else s2[i]]
     j+=1
   else:
     s3+=[s2[i]]
 return ''.join(s3)

